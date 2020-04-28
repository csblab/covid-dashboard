#!/usr/bin/python

import dash
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
import dash_core_components as dcc
import dash_table
import dash_html_components as html
import pathlib
import re
import numpy as np
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go


def get_date_columns(dataframe):
    date_regex = re.compile('\d{1,2}/\d{1,2}/\d{2,4}')
    cols = dataframe.columns
    return [c for i, c in enumerate(cols) if date_regex.match(c)]  # indexes of the date cols


# Data Transformations

def get_change_per_day(data):
    return [0] + (data[1:] - data[:-1]).tolist()


def get_log(data):
    v = np.log10(data + 1e-10)
    return v


def pickdataframe(smoothwindow):
    df = f'{smoothwindow}'
    return df


def plot_country(country, countryname, smoothing, yvals, y2vals):
    
    yvals_log = get_log(yvals)
    y2vals_log = get_log(y2vals)
    
    # Per-day change
    yvals_perday = get_change_per_day(yvals)
    y2vals_perday = get_change_per_day(y2vals)
    
    fig = make_subplots(rows=3, cols=1, 
                        shared_xaxes=True,
                        specs=[[{"secondary_y": True}],
                               [{"secondary_y": True}],
                               [{"secondary_y": True}]],
                               vertical_spacing = 0.03)
                                
    fig.add_trace(
                    go.Scatter(x=date_cols, y= yvals_perday,
                    mode='lines+markers',
                    name='Daily New Confirmed Cases',
                    line=dict(color='#ff112d', width=2)),
                    secondary_y=False,
                    row=1, col=1 
                )
    fig.add_trace(
                    go.Scatter(x=date_cols, y=y2vals_perday,
                    mode='lines+markers',
                    name='Daily New Deaths (right axis)',
                    line=dict(color='black', width=2)),
                    secondary_y=True,
                    row=1, col=1 
                )

    fig.add_trace(
                    go.Scatter(x=date_cols, y=yvals,
                    mode='lines+markers',
                    name='Total Confirmed',
                    line=dict(color='#0e59ef', width=2)),
                    secondary_y=False,
                    row=2, col=1
                )
    fig.add_trace(
                    go.Scatter(x=date_cols, y=y2vals,
                    mode='lines+markers',
                    name='Total Deaths (right axis)',
                    line=dict(color='black', width=2)),
                    secondary_y=True,
                    row=2, col=1
                )
    fig.add_trace(
                    go.Scatter(x=date_cols, y=yvals_log,
                    mode='lines+markers',
                    name='log10(Total Confirmed)',
                    line=dict(color='#0eefd9', width=2)),
                    secondary_y=False,
                    row=3, col=1
                )
    fig.add_trace(
                    go.Scatter(x=date_cols, y=y2vals_log,

                    mode='lines+markers',
                    name='log10(Total Deaths) (right axis)',
                    line=dict(color='black', width=2)),
                    secondary_y=True,
                    row=3, col=1
                )
    fig.update_yaxes( range=[0, yvals_log[-1]+1], row=3, col=1)
    
    fig.update_annotations(dict(font_size=8))

    fig.update_layout(
        height=600,
        #width=800,
        title_text=f'{countryname} ({smoothing})'

    )
    return fig
    #return [fig]

def get_dates_window(dateslist, n=6):
    d = len(dateslist)-n
    dates = dateslist[d:]
    return dates


def format_table(df, dates, window=3):
    # We make a new dataframe to store the results
    df_ratio = pd.DataFrame(
        columns=['Country_Region', 'Confirmed', 
                 'C_Ratio', 'Deaths', 'D_Ratio']
    )

    
    country_list = list(df['Country_Region_Safe'].unique())

    for i, country in enumerate(country_list):

        confirmed = df[(df['Country_Region_Safe'] == country) & (df['Case_Type'] == 'Confirmed')][dates[-1]]
        deaths = df[(df['Country_Region_Safe'] == country) & (df['Case_Type'] == 'Deaths')][dates[-1]]

        country_orig = df[(df['Country_Region_Safe'] == country) & (df['Case_Type'] == 'Confirmed')]['Country_Region']

        # calc ratio for deaths

        maskd = (df['Country_Region_Safe'] == country) & (df['Case_Type'] == 'Deaths')
        first3 = np.asarray(df[maskd][dates[0:window]].iloc[-1].to_list()).mean()
        last3 = np.asarray(df[maskd][dates[window:]].iloc[-1].to_list()).mean() + 0.0000001
        ratiod = (last3/first3)

        # calc ratio for cases
        maskc = (df['Country_Region_Safe'] == country) & (df['Case_Type'] == 'Confirmed')
        last3 = np.asarray(df[maskc][dates[0:window]].iloc[-1].to_list()).mean() 
        first3 = np.asarray(df[maskc][dates[window:]].iloc[-1].to_list()).mean() + 0.0000001
        ratioc = (last3/first3)

        try:
            datadict = {
                    'Country_Region': country_orig.iloc[-1],
                    'Confirmed': confirmed.iloc[-1],
                    'C_Ratio': ratioc.round(3),
                    'Deaths': deaths.iloc[-1],
                    'D_Ratio': ratiod.round(3),
            }

        except Exception as err:
            #print(f'Could not calculate ratios for {country}: {err}')
            continue

        df_ratio = df_ratio.append(datadict, ignore_index=True)

    return df_ratio


def plot_country_by_smoothing(country, smoothing, dfdict, datecols):
    df = dfdict[smoothing]
    #country = 'Israel'
    country_mask = df['Country_Region'] == country

    cmask = country_mask & (df['Case_Type'] == 'Confirmed')
    dmask = country_mask & (df['Case_Type'] == 'Deaths')

    cvals = df.loc[cmask].groupby('Country_Region_Safe').sum().values[0, :]
    dvals = df.loc[dmask].groupby('Country_Region_Safe').sum().values[0, :]

    f = plot_country(country, smoothing, datecols, cvals, dvals)
    return f



########################################################################################
########################################################################################


THRESH = 50 # Threshold for minimum number of cases/deaths
DISPLAY = 'Countries' #'Countries' Choose 'All' for US Italy and China regions / 'Countries' for just countries
# set directories and file paths
rootdir = pathlib.Path('.') 
output_dir = rootdir / 'data'  # directory where the csv files are

prefixes = ["UNS", "SMO3", "SMO7"]

data_by_smoothing = {
        "UNS": "",
        "SMO3": "",
        "SMO7": "",
    }

if DISPLAY == 'Countries':

    fnamelist = [
        'Data_COVID-19_v2_bycountry.csv',
        'Data_COVID-19_v2_bycountry_smooth_3.csv',
        'Data_COVID-19_v2_bycountry_smooth_7.csv'
    ]
if DISPLAY == 'All':

    fnamelist = [
        'Data_COVID-19_v2_merged.csv',
        'Data_COVID-19_v2_merged_smooth_3.csv',
        'Data_COVID-19_v2_merged_smooth_7.csv',
    ]

fpathlist = [ output_dir / fname for fname in fnamelist ]

for i, prefix in enumerate(prefixes):
    csv_fpath = fpathlist[i]
    try:
        csv_fullpath = csv_fpath.resolve(strict=True)
    except FileNotFoundError:
        #print(f'CSV file not found: {csv_fpath}')
        raise
    else:
        df = pd.read_csv(csv_fpath)

    data_by_smoothing[prefix] = df


date_cols = get_date_columns(df)
 
dates = get_dates_window(date_cols, 3)

d = len(date_cols)-6
dates = date_cols[d:]

df_ratio = format_table(df, dates, 3)

# Remove countries with less than N deaths
mask_deaths = df_ratio['Deaths'] > THRESH
df_ratio = df_ratio[mask_deaths]

#Create Dash/Flask app

app = dash.Dash(__name__)
server = app.server #for server deployment

app.layout = html.Div(
    id="content",
    children=[

        html.Div(
            id="title",
            children=[
                html.H2(
                    'Visualization of COVID-19 data'),
            ]
        ),

        html.Button('Clear selection', id='clear-button'),

        dash_table.DataTable(

            id='datatable-interactivity-ids',

            columns=[
                  {"name": i, "id": i, "selectable": True} for i in df_ratio.columns
            ],

            data=df_ratio.to_dict('records'),

            hidden_columns=['_smoothindex'],

            fill_width = True,

            style_header={
                         'textAlign': 'center', 
                         'backgroundColor': 'rgb(50, 50, 50)',
                         'color': 'white'
            },

            fixed_rows={ 'headers': True, 'data': 0 },

            style_cell={
                    'overflow': 'hidden',
                    'textOverflow': 'ellipsis', 
                    'maxWidth': 0,
                    'textAlign': 'center',
                    'backgroundColor': 'rgb(239,239,239)',
                    'color': 'black'
            },

            style_table={
               'maxHeight': '400px',
               #'maxWidth': '1400px',
               'overflowY': 'scroll',
               'border': 'thin lightgrey solid'
            },

            style_cell_conditional=[

                {'if': {'column_id': 'Confirmed'}, 'width': '10%'},
                {'if': {'column_id': 'Deaths'}, 'width': '10%'},
                {'if': {'column_id': 'C_Ratio'}, 'width': '10%'},
                {'if': {'column_id': 'D_Ratio'}, 'width': '10%'}, 
                {'if': {'column_id': 'Category'}, 'width': '10%'},
                { 'if' :{'column_id': 'Country_Region'},'textAlign': 'left'},

            ],
 
            filter_action="native",
            sort_action="custom",
            sort_by=[],
            sort_mode="multi",
            row_selectable="multi",
            selected_rows=[],
            page_action="native",
        ),

        dcc.RadioItems(
            id='smooth-level-radio',
            options=[
                {'label': 'Raw', 'value': 'UNS'},
                {'label': 'Smooth 3', 'value': 'SMO3'},
                {'label': 'Smooth 7', 'value': 'SMO7'}
            ],
            value='UNS'
        ),

        html.Div(id='plot-container', style={'width': '100%', 'display': 'flex', 'flex-wrap': 'wrap'}),
    ]
)

#Callbacks

# sort 
@app.callback(
    
    Output('datatable-interactivity-ids', "data"),

    [
        Input('datatable-interactivity-ids', "sort_by")
    ]
)
def sort_table(sort_cols):
    # sort_cols is a list of dicts
    # with colname and and order

    if not sort_cols:
        return df_ratio.to_dict('records')  # cheaper

    # Do sorting by selected columns
    sort_by_cols = []
    sort_order = []
    for col in sort_cols:
        cid = col["column_id"]
        if cid == "Smoothing":
            cid = "_smoothindex"
        corder = col["direction"] == "asc"
        sort_by_cols.append(cid)
        sort_order.append(corder)

    # Sort dataframe
    df_ratio.sort_values(sort_by_cols, ascending=sort_order, inplace=True)
    return df_ratio.to_dict('records')


# clear button
@app.callback(
    
    Output('datatable-interactivity-ids', "selected_rows"),

    [
        Input('clear-button', 'n_clicks')
    ]
)
def clear_selection(a):
    return []

# plot
@app.callback(
    Output("plot-container", "children"),
    [
        Input('datatable-interactivity-ids', "data"),
        Input('datatable-interactivity-ids', "selected_rows"),
        Input('smooth-level-radio', 'value'),
    ],
)

def plot_country_by_smoothing(tbl_df, countries, smoothlevel):

    """Updates plots with options from click-row """

    if not countries:
        raise PreventUpdate

    fig_lst = []
    # country = countries[0]  # this should be a for loop

    for country in countries:

        country_name = tbl_df[country]['Country_Region']

        df = data_by_smoothing[smoothlevel]
        country_mask = (df['Country_Region'] == country_name)

        cmask = country_mask & (df['Case_Type'] == 'Confirmed')
        dmask = country_mask & (df['Case_Type'] == 'Deaths')

        cvals = df.loc[cmask].groupby('Country_Region_Safe').sum().values[0, :]
        dvals = df.loc[dmask].groupby('Country_Region_Safe').sum().values[0, :]

        cvals_log = get_log(cvals)
        dvals_log = get_log(dvals)

        # Per-day change
        cvals_perday = get_change_per_day(cvals)
        dvals_perday = get_change_per_day(dvals)


        fig = plot_country(country, country_name, smoothlevel, cvals, dvals)
        fig_lst.append(dcc.Graph(figure=fig)) 

    
    #return dcc.Graph(figure=fig)
    return fig_lst


if __name__ == '__main__':
    app.run_server(debug=False)

