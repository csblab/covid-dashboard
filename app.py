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
    """Makes 3-panel plot from country data"""

    # Log values
    yvals_log = get_log(yvals)
    y2vals_log = get_log(y2vals)

    # Per-day change
    yvals_perday = get_change_per_day(yvals)
    y2vals_perday = get_change_per_day(y2vals)

    fig = make_subplots(
        rows=3,
        cols=1,
        shared_xaxes=True,
        specs=[
            [{"secondary_y": True}],
            [{"secondary_y": True}],
            [{"secondary_y": True}]
        ],
        vertical_spacing=0.03
    )

    fig.add_trace(
        go.Scatter(
            x=date_cols,
            y=yvals_perday,
            mode='lines',
            name='Daily New Confirmed Cases',
            line=dict(color='#ff112d', width=2)
        ),
        secondary_y=False,
        row=1,
        col=1
    )
    fig.add_trace(
        go.Scatter(
            x=date_cols,
            y=y2vals_perday,
            mode='lines',
            name='Daily New Deaths (right axis)',
            line=dict(color='black', width=2)
        ),
        secondary_y=True,
        row=1,
        col=1
    )

    fig.add_trace(
        go.Scatter(
            x=date_cols,
            y=yvals,
            mode='lines',
            name='Total Confirmed',
            line=dict(color='#0e59ef', width=2)
        ),
        secondary_y=False,
        row=2,
        col=1
    )

    fig.add_trace(
        go.Scatter(
            x=date_cols,
            y=y2vals,
            mode='lines',
            name='Total Deaths (right axis)',
            line=dict(color='black', width=2)
        ),
        secondary_y=True,
        row=2,
        col=1
    )

    fig.add_trace(
        go.Scatter(
            x=date_cols,
            y=yvals_log,
            mode='lines',
            name='log10(Total Confirmed)',
            line=dict(color='#0eefd9', width=2)
        ),
        secondary_y=False,
        row=3,
        col=1
    )

    fig.add_trace(
        go.Scatter(
            x=date_cols,
            y=y2vals_log,
            mode='lines',
            name='log10(Total Deaths) (right axis)',
            line=dict(color='black', width=2)
        ),
        secondary_y=True,
        row=3,
        col=1
    )

    fig.update_yaxes(
        range=[0, yvals_log[-1]+1],
        row=3,
        col=1
    )

    fig.update_annotations(dict(font_size=8))

    fig.update_layout(
        height=600,
        width=500,
        margin={'l':0,'b':15,'r':10},
        title_text=f'{countryname} ({smoothing})',
        legend=dict(
                bgcolor='rgba(0,0,0,0)',
                orientation="h",
                x=0, y=-0.2),
    )
    return fig


def get_dates_window(dateslist, n=6):
    d = len(dateslist)-n
    dates = dateslist[d:]
    return dates


def format_table(df, dates, window=3, min_deaths=50):
    # We make a new dataframe to store the results


    # filter for min deaths
    deathsonly = df[df['Case_Type'] == 'Deaths']
    min_death_mask = deathsonly[dates[-1]] >= min_deaths
    keepers = deathsonly[min_death_mask]['Fullname_Safe'].unique()
    keepmask = df['Fullname_Safe'].isin(keepers)
    df = df[keepmask]

    entry_list = list(df['Fullname_Safe'].unique())
    confirmed_mask = df['Case_Type'] == 'Confirmed'
    death_mask = df['Case_Type'] == 'Deaths' 
    
    records = []
    for i, entry in enumerate(entry_list):
        country_mask = df['Fullname_Safe'] == entry
        

        country_confirmed_mask = country_mask & confirmed_mask
        country_deaths_mask = country_mask & death_mask

        confirmed = df[country_mask & confirmed_mask]
        deaths = df[country_mask & death_mask]

        country_orig = df[country_mask & confirmed_mask]['Fullname_Safe']

        # calc ratio for deaths
        first_dates = dates[0:window]
        last_dates = dates[window:]

        first3 = df[country_deaths_mask][first_dates].mean(axis=1).item()
        last3 = df[country_deaths_mask][last_dates].mean(axis=1).item()
        ratiod = last3 / (first3 + 1e-10)

        # calc ratio for cases
        first3 = df[country_confirmed_mask][first_dates].mean(axis=1).item()
        last3 = df[country_confirmed_mask][last_dates].mean(axis=1).item()
        ratioc = last3 / (first3 + 1e-10)

        datadict = {
                'Location': country_orig.iloc[-1],
                'Confirmed': confirmed[date_cols[-1]].item(),
                'C_Ratio': round(ratioc, 3),
                'Deaths': deaths[date_cols[-1]].item(),
                'D_Ratio': round(ratiod, 3),
        }

        records.append(datadict)

    df_ratio = pd.DataFrame.from_records(
            data=records,
            columns=[
                    'Location',
                    'Confirmed',
                    'C_Ratio',
                    'Deaths',
                    'D_Ratio'
            ]
    )
    return df_ratio


###############################################################################
###############################################################################


THRESH = 50  # Threshold for minimum number of cases/deaths
DISPLAY = 'All'  #'Countries' Choose 'All' for US Italy and China regions / 'Countries' for just countries
# set directories and file paths
rootdir = pathlib.Path('.')
output_dir = rootdir / 'data'  # directory where the csv files are

prefixes = ["UNS", "SMO3", "SMO7", "SMO9"]

data_by_smoothing = {
        "UNS": "",
        "SMO3": "",
        "SMO7": "",
        "SMO9": "",
    }

if DISPLAY == 'Countries':

    fnamelist = [
        'Data_COVID-19_v2_bycountry_smooth_3.csv',
        'Data_COVID-19_v2_bycountry.csv',
        'Data_COVID-19_v2_bycountry_smooth_7.csv'
        'Data_COVID-19_v2_bycountry_smooth_9.csv'
    ]

elif DISPLAY == 'All':
    fnamelist = [
        'Data_COVID-19_v2.csv',
        'Data_COVID-19_v2_smooth_3.csv',
        'Data_COVID-19_v2_smooth_7.csv',
        'Data_COVID-19_v2_smooth_9.csv',
    ]

fpathlist = [ output_dir / fname for fname in fnamelist ]

for i, prefix in enumerate(prefixes):
    csv_fpath = fpathlist[i]
    try:
        csv_fullpath = csv_fpath.resolve(strict=True)
    except FileNotFoundError:
        raise
    else:
        df = pd.read_csv(csv_fpath)
        df.drop(['Source', 'Last_Update_Date'], axis=1, inplace=True)
        # Group countries

        countries = df.groupby(
            ['Country_Region', 'Case_Type', 'Country_Region_Safe']
        ).sum().reset_index()
        # Get Province data
        state_level_mask = (
            ~df['Province_State_Safe'].isna() & df['County_Name_Safe'].isna()
        )
        # Get County Data
        county_level_mask = (
            ~df['Province_State_Safe'].isna() & ~df['County_Name_Safe'].isna()
        )

        # Mask mega dataframe
        combined = countries.append(
            df[state_level_mask]
        ).append(df[county_level_mask])
        # Make FullName Safe column
        pss_clean = combined['Province_State_Safe'].fillna(value='')
        cns_clean = combined['County_Name_Safe'].fillna(value='')
        combined['Fullname_Safe'] = (
            combined['Country_Region_Safe'] + '_' +
            pss_clean + '_' + cns_clean
        )
        combined['Fullname_Safe'] = combined['Fullname_Safe'].str.strip('_')

    data_by_smoothing[prefix] = combined
    del df
    del countries


date_cols = get_date_columns(combined)
 
dates = get_dates_window(date_cols, 3)

d = len(date_cols)-6
dates = date_cols[d:]

df_ratio = format_table(combined, dates, 4)

#Classify cuntries by category

df_ratio['Category'] = None

cat_criteria = {
  
  #  'cC': lambda d: (d['C_Ratio'] >= 1.07),# & (d['D_Ratio'] >= 1.01),
   # 'stableC': lambda d: (d['C_Ratio'] > 1.07) & (d['C_Ratio'] < 1.1),# & (d['C_Ratio'] < 1.01) & (d['D_Ratio'] >= 0.99) & (d['D_Ratio'] < 1.01 ),
  #  'cc': lambda d: (d['C_Ratio'] <= 1.07),# & (d['D_Ratio'] < 0.99),
    'cCdD': lambda d: (d['C_Ratio'] >= 1.07) & (d['D_Ratio'] >= 1.017), 
    'cCdd': lambda d: (d['C_Ratio'] >= 1.07) & (d['D_Ratio'] <= 1.017),
    'ccdD': lambda d: (d['C_Ratio'] <= 1.07) & (d['D_Ratio'] >= 1.017),
    'ccdd': lambda d: (d['C_Ratio'] <= 1.07) & (d['D_Ratio'] <= 1.017)
}

for catname, catfunc in cat_criteria.items():
    mask = catfunc(df_ratio)
    df_ratio.loc[mask, 'Category'] = catname


#Create Dash/Flask app

app = dash.Dash(__name__)
server = app.server  #for server deployment

app.layout = html.Div(
    id="content",
    children=[

        html.Div(
            id="title",
            style={'backgroundColor': '#36393b'},
            children=[
                html.H1(
                    'Visualization of COVID-19 data',
                    style={
                           'color':  '#e6f6fc', 
                           'font-family': 'Courier',
                           'font-weight': 'bold',
                           'font-size': '35px',
                           'textAlign': 'center',
                           }
                ) 
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
            css=[{"selector": ".show-hide", "rule": "display: none"}],

            fill_width = True,

            style_header={
                         'textAlign': 'center', 
                         'font_size': '18px',
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
                    'color': 'black',
            },
            style_data={
                    #'font_family': 'cursive',
                    'font_size': '18px',
                    #'text_align': 'left'

            },

            style_table={
               'maxHeight': '400px',
               #'maxWidth': '1400px',
               'overflowY': 'scroll',
               'border': 'thin lightgrey solid'
            },

            style_cell_conditional=[

                {'if': {'column_id': 'Confirmed'}, 'width': '10%', 'textAlign': 'center'},
                {'if': {'column_id': 'Deaths'}, 'width': '10%', 'textAlign': 'center'},
                {'if': {'column_id': 'C_Ratio'}, 'width': '10%', 'textAlign': 'center'},
                {'if': {'column_id': 'D_Ratio'}, 'width': '10%', 'textAlign': 'center'}, 
                {'if': {'column_id': 'Category'}, 'width': '10%', 'textAlign': 'center'},
                { 'if' :{'column_id': 'Location'}, 'textAlign': 'left'},

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
                {'label': 'Smooth 7', 'value': 'SMO7'},
                {'label': 'Smooth 9', 'value': 'SMO9'}
            ],
            value='SMO9'
        ),


        html.Div(
            id='plot-container',
            style={
                'width': '100%',
                'display': 'flex',
                'flex-wrap': 'wrap'
            }
        ),

    ]
)


# Callbacks

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
        Input('clear-button', 'n_clicks'),
    ],
)
def plot_country_by_smoothing(tbl_df, countries, smoothlevel, click_clear):
    """Updates plots with options from click-row """

    fig_lst = []
    # Was the clear button clicked?
    is_clear = any(
        p['prop_id'] == 'clear-button.n_clicks'
        for p in dash.callback_context.triggered
    )

    if is_clear:
        return fig_lst

    if not countries:
        raise PreventUpdate

    df = data_by_smoothing[smoothlevel]
    for country in countries:

        country_name = tbl_df[country]['Location']
        country_mask = (df['Fullname_Safe'] == country_name)

        cmask = country_mask & (df['Case_Type'] == 'Confirmed')
        dmask = country_mask & (df['Case_Type'] == 'Deaths')

        # date_cols is global
        cvals = df.loc[cmask][date_cols].values[0, :]
        dvals = df.loc[dmask][date_cols].values[0, :]

        fig = plot_country(country, country_name, smoothlevel, cvals, dvals)
        fig_lst.append(dcc.Graph(figure=fig))

    return fig_lst


if __name__ == '__main__':
    app.run_server(debug=False)
