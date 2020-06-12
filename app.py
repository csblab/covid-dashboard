import dash
import dash_core_components as dcc
import dash_flexbox_grid as dfx
import dash_html_components as html
import flask
import glob
import os
import pathlib
import numpy as np
import pandas as pd
import re

# FUNCTIONS

def get_date_columns(dataframe):
    date_regex = re.compile('\d{1,2}/\d{1,2}/\d{2,4}')
    cols = dataframe.columns
    return [c for i, c in enumerate(cols) if date_regex.match(c)]  # indexes of the date cols


scriptdir = pathlib.Path(os.getcwd())  # this notebook

image_directory_us = scriptdir / 'plots_gp/US/'
list_of_images_us = sorted([str(f).split('/US/')[1] for f in list(image_directory_us.rglob('*.png'))])
static_image_route_us = '/staticUS/'

image_directory_world = scriptdir / 'plots_gp/World/'
list_of_images_world = sorted([str(f).split('/World/')[1] for f in list(image_directory_world.rglob('*.png'))])
static_image_route_world = '/staticWD/'

image_directory_italy = scriptdir / 'plots_gp/Italy/'
list_of_images_italy = sorted([str(f).split('/Italy/')[1] for f in list(image_directory_italy.rglob('*.png'))])
static_image_route_italy = '/staticIT/'

image_directory_canada = scriptdir / 'plots_gp/Canada/'
list_of_images_canada = sorted([str(f).split('/Canada/')[1] for f in list(image_directory_canada.rglob('*.png'))])
static_image_route_canada = '/staticCA/'

image_directory_s_america = scriptdir / 'plots_gp/South_America/'
list_of_images_s_america = sorted([str(f).split('/South_America/')[1] for f in list(image_directory_s_america.rglob('*.png'))])
static_image_route_s_america = '/staticSA/'


# Threshold for minimum number of cases/deaths
DTHRESH = 50

rootdir = pathlib.Path('.')
output_dir = rootdir / 'data'  # directory where the csv files are

csv_fpath = output_dir / 'Select_COVID_data_PEAKS.csv'

try:
    csv_fullpath = csv_fpath.resolve(strict=True)
except FileNotFoundError:
    print(f'CSV file not found: {csv_fpath}')
    raise
else:
    df = pd.read_csv(csv_fpath)

date_cols = get_date_columns(df)
last_date = date_cols[-1]
last_date_index = date_cols.index(last_date) + 1

removed_cols = ['Source', 'Last_Update_Date']

df.drop(removed_cols, axis=1, inplace=True)


deathsonly = df[df['Case_Type'] == 'Deaths']
dates = get_date_columns(df)
last_date = dates[-1]
min_death_mask = deathsonly[dates[-1]] >= DTHRESH
keepers = deathsonly[min_death_mask]['Country_Region_Safe'].unique()
keepmask = df['Country_Region_Safe'].isin(keepers)
df_filter = df[keepmask]


# Make table for app display
entry_list = list(df_filter['Country_Region_Safe'].unique())

confirmed_mask = df_filter['Case_Type'] == 'Confirmed'
death_mask = df_filter['Case_Type'] == 'Deaths'

records = []
for i, entry in enumerate(entry_list):

        country_mask = df_filter['Country_Region_Safe'] == entry

        confirmed = df_filter[country_mask & confirmed_mask]
        deaths = df_filter[country_mask & death_mask]
        country_code_mask = df_filter.loc[country_mask, 'Classification_Code']
        country_smoothing_mask = df_filter.loc[country_mask, 'Smoothing']
        country_start_mask_c = df_filter.loc[country_mask, 'Start_Cases']
        country_peak_mask_c = df_filter.loc[country_mask, 'Peak_Cases']
        country_start_mask_d = df_filter.loc[country_mask, 'Start_Deaths']
        country_peak_mask_d = df_filter.loc[country_mask, 'Peak_Deaths']
        country_deaths_per_case_mask = df_filter.loc[country_mask, 'Deaths_per_Case']
        country_display = df_filter.loc[country_mask, 'Country_Region']
        datadict = {
                 'Location1': entry,
                 'Location': country_display.to_list()[-1],
                 'Smoothing': country_smoothing_mask.to_list()[-1],
                 'Class': country_code_mask.to_list()[-1],
                 #'Cases': confirmed['nCases'].item(),
                 'Cases': int(confirmed[last_date].to_list()[-1]),
                 'Start_C': country_start_mask_c.to_list()[-1],
                 'Peak_C': country_peak_mask_c.to_list()[-1],
                 'Deaths': deaths['nDeaths'].item(),
                 #s'Deaths': int(deaths[last_date].to_list()[-1]),
                 'Start_D': country_start_mask_d.to_list()[-1],
                 'Peak_D': country_peak_mask_d.to_list()[-1],
                 'Deaths/Cases(%)':  country_deaths_per_case_mask.to_list()[-1]
        }
        records.append(datadict)

df_ratio = pd.DataFrame.from_records(
        data=records,
        columns=[
            'Location1',
            'Location',
            'Smoothing',
            'Class',
            'Cases',
            'Start_C',
            'Peak_C',
            'Deaths',
            'Start_D',
            'Peak_D',
            'Deaths/Cases(%)', 
        ]
)


app = dash.Dash(__name__)
server = app.server #for server deployment
app.scripts.config.serve_locally = True


tabs_styles = {
    'height': '44px'
}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold',
    'padding': '10px',
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#ff7a7a',
    'color': 'white',
    'padding': '10px',
    'align-items': 'center',
    'fontWeight': 'bold',
}

app.layout =  html.Div([
     dcc.Tabs(
        id="tabs-styled-with-inline",
        children=[
            dcc.Tab(
                label='Table',
                value='tab-1',
                style=tab_style,
                selected_style=tab_selected_style,                
            ),
            dcc.Tab(
                label='WORLD',
                value='tab-2',
                style=tab_style,
                selected_style=tab_selected_style,
                children=[
                    dfx.Grid(
                        id='grid',
                        fluid=True,
                        children=[
                            dfx.Row(
                                id='row1-1-1',
                                children=[
                                    dfx.Col(
                                        id='col1-1-1',
                                            xs=6,
                                            lg=6,
                                            children=[
                                                html.H3('Location 1'),
                                                    dcc.Dropdown(
                                                        id='image-dropdownWorld1',
                                                        options=[{'label': i, 'value': i} for i in list_of_images_world],
                                                        placeholder="Select Country",
                                                        value=list_of_images_world[0],
                                                        style=dict(
                                                           width='90%',
                                                           #display='inline-block',
                                                           verticalAlign="middle"
                                                        )
                                                    ),
                                                html.Img(id='imageworld1', style={'width': '600px'})
                                            ],
                                    ),
                                    dfx.Col(
                                        id='col1-1-2',
                                            xs=6,
                                            lg=6,
                                            children=[
                                                html.H3('Location 2'),
                                                    dcc.Dropdown(
                                                        id='image-dropdownWorld2',
                                                        options=[{'label': i, 'value': i} for i in list_of_images_world],
                                                        placeholder="Select Country",
                                                        value=list_of_images_world[1],
                                                        style=dict(
                                                           width='90%',
                                                           #display='inline-block',
                                                           verticalAlign="middle"
                                                        )
                                                    ),
                                                html.Img(id='imageworld2', style={'width': '600px'})
                                            ],
                                    ),
                                ],
                                
                            ),
                            dfx.Row(
                                id='row1-1-2',
                                children=[
                                    dfx.Col(
                                        id='col1-2-1',
                                            xs=6,
                                            lg=6,
                                            children=[
                                                html.H3('Location 3'),
                                                    dcc.Dropdown(
                                                        id='image-dropdownWorld3',
                                                        options=[{'label': i, 'value': i} for i in list_of_images_world],
                                                        placeholder="Select Country",
                                                        value=list_of_images_world[2],
                                                        style=dict(
                                                           width='90%',
                                                           #display='inline-block',
                                                           verticalAlign="middle"
                                                        )
                                                    ),
                                                html.Img(id='imageworld3', style={'width': '600px'})
                                            ],
                                        ),
                                    dfx.Col(
                                        id='col1-2-2',
                                            xs=6,
                                            lg=6,
                                            children=[
                                                html.H3('Location 4'),
                                                    dcc.Dropdown(
                                                        id='image-dropdownWorld4',
                                                        options=[{'label': i, 'value': i} for i in list_of_images_world],
                                                        placeholder="Select Country",
                                                        value=list_of_images_world[3],
                                                        style=dict(
                                                           width='90%',
                                                           #display='inline-block',
                                                           verticalAlign="middle"
                                                        )
                                                    ),
                                                html.Img(id='imageworld4', style={'width': '600px'})
                                            ],
                                        ),
                                ],
                                
                            ),
                            dfx.Row(
                                id='row1-1-3',
                                children=[
                                    dfx.Col(
                                        id='col1-3-1',
                                            xs=6,
                                            lg=6,
                                            children=[
                                                html.H3('Location 5'),
                                                    dcc.Dropdown(
                                                        id='image-dropdownWorld5',
                                                        options=[{'label': i, 'value': i} for i in list_of_images_world],
                                                        placeholder="Select Country",
                                                        value=list_of_images_world[4],
                                                        style=dict(
                                                           width='90%',
                                                           #display='inline-block',
                                                           verticalAlign="middle"
                                                        )
                                                    ),
                                                html.Img(id='imageworld5', style={'width': '600px'})
                                            ],
                                        ),
                                    dfx.Col(
                                        id='col1-3-2',
                                            xs=6,
                                            lg=6,
                                            children=[
                                                html.H3('Location 6'),
                                                    dcc.Dropdown(
                                                        id='image-dropdownWorld6',
                                                        options=[{'label': i, 'value': i} for i in list_of_images_world],
                                                        placeholder="Select Country",
                                                        value=list_of_images_world[5],
                                                        style=dict(
                                                           width='90%',
                                                           #display='inline-block',
                                                           verticalAlign="middle"
                                                        )
                                                    ),
                                                html.Img(id='imageworld6', style={'width': '600px'})
                                            ],
                                        ),
                                ],
                                
                            ),

                        ],
                    ),
                ],
            ),
            dcc.Tab(
                label='US',
                value='tab-3',
                style=tab_style,
                selected_style=tab_selected_style,
                children=[
                   dfx.Grid(
                        children=[
                            dfx.Row(
                                id='row2-1-1',
                                children=[
                                    dfx.Col(
                                        id='col2-1-1',
                                            xs=6,
                                            lg=6,
                                            children=[
                                                html.H3('Location 1'),
                                                    dcc.Dropdown(
                                                        id='image-dropdownUS1',
                                                        options=[{'label': i, 'value': i} for i in list_of_images_us],
                                                        placeholder="Select Country",
                                                        value=list_of_images_us[0],
                                                        style=dict(
                                                           width='90%',
                                                           #display='inline-block',
                                                           verticalAlign="middle"
                                                        )
                                                    ),
                                                html.Img(id='imageus1', style={'width': '600px'})
                                            ],
                                        ),
                                    dfx.Col(
                                        id='col2-1-2',
                                            xs=6,
                                            lg=6,
                                            children=[
                                                html.H3('Location 2'),
                                                    dcc.Dropdown(
                                                        id='image-dropdownUS2',
                                                        options=[{'label': i, 'value': i} for i in list_of_images_us],
                                                        placeholder="Select Country",
                                                        value=list_of_images_us[1],
                                                        style=dict(
                                                           width='90%',
                                                           #display='inline-block',
                                                           verticalAlign="middle"
                                                        )
                                                    ),
                                                html.Img(id='imageus2', style={'width': '600px'})
                                            ],
                                        ),
                                ],
                                
                            ),
                            dfx.Row(
                                id='row2-1-2',
                                children=[
                                    dfx.Col(
                                        id='col2-2-1',
                                            xs=6,
                                            lg=6,
                                            children=[
                                                html.H3('Location 3'),
                                                    dcc.Dropdown(
                                                        id='image-dropdownUS3',
                                                        options=[{'label': i, 'value': i} for i in list_of_images_us],
                                                        placeholder="Select Country",
                                                        value=list_of_images_us[2],
                                                        style=dict(
                                                           width='90%',
                                                           #display='inline-block',
                                                           verticalAlign="middle"
                                                        )
                                                    ),
                                                html.Img(id='imageus3', style={'width': '600px'})
                                            ],
                                        ),
                                    dfx.Col(
                                        id='col2-2-2',
                                            xs=6,
                                            lg=6,
                                            children=[
                                                html.H3('Location 4'),
                                                    dcc.Dropdown(
                                                        id='image-dropdownUS4',
                                                        options=[{'label': i, 'value': i} for i in list_of_images_us],
                                                        placeholder="Select Country",
                                                        value=list_of_images_us[3],
                                                        style=dict(
                                                           width='90%',
                                                           #display='inline-block',
                                                           verticalAlign="middle"
                                                        )
                                                    ),
                                                html.Img(id='imageus4', style={'width': '600px'})
                                            ],
                                        ),
                                ],
                                
                            ),
                            dfx.Row(
                                id='row2-1-3',
                                children=[
                                    dfx.Col(
                                        id='col2-3-1',
                                            xs=6,
                                            lg=6,
                                            children=[
                                                html.H3('Location 5'),
                                                    dcc.Dropdown(
                                                        id='image-dropdownUS5',
                                                        options=[{'label': i, 'value': i} for i in list_of_images_us],
                                                        placeholder="Select Country",
                                                        value=list_of_images_us[4],
                                                        style=dict(
                                                           width='90%',
                                                           #display='inline-block',
                                                           verticalAlign="middle"
                                                        )
                                                    ),
                                                html.Img(id='imageus5', style={'width': '600px'})
                                            ],
                                        ),
                                    dfx.Col(
                                        id='col2-3-2',
                                            xs=6,
                                            lg=6,
                                            children=[
                                                html.H3('Location 6'),
                                                    dcc.Dropdown(
                                                        id='image-dropdownUS6',
                                                        options=[{'label': i, 'value': i} for i in list_of_images_us],
                                                        placeholder="Select Country",
                                                        value=list_of_images_us[5],
                                                        style=dict(
                                                           width='90%',
                                                           #display='inline-block',
                                                           verticalAlign="middle"
                                                        )
                                                    ),
                                                html.Img(id='imageus6', style={'width': '600px'})
                                            ],
                                        ),
                                ],
                                
                            ),

                        ],


                   ),
                ]
            ),
            dcc.Tab(
                label='ITALY',
                value='tab-4',
                style=tab_style,
                selected_style=tab_selected_style,
                children=[
                    dfx.Grid(
                        children=[
                            dfx.Row(
                                id='row3-1-1',
                                children=[
                                    dfx.Col(
                                        id='col3-1-1',
                                            xs=6,
                                            lg=6,
                                            children=[
                                                html.H3('Location 1'),
                                                    dcc.Dropdown(
                                                        id='image-dropdownIT1',
                                                        options=[{'label': i, 'value': i} for i in list_of_images_italy],
                                                        placeholder="Select Country",
                                                        value=list_of_images_italy[0],
                                                        style=dict(
                                                           width='90%',
                                                           #display='inline-block',
                                                           verticalAlign="middle"
                                                        )
                                                    ),
                                                html.Img(id='imageit1', style={'width': '600px'})
                                            ],
                                        ),
                                    dfx.Col(
                                        id='col3-1-2',
                                            xs=6,
                                            lg=6,
                                            children=[
                                                html.H3('Location 2'),
                                                    dcc.Dropdown(
                                                        id='image-dropdownIT2',
                                                        options=[{'label': i, 'value': i} for i in list_of_images_italy],
                                                        placeholder="Select Country",
                                                        value=list_of_images_italy[1],
                                                        style=dict(
                                                           width='90%',
                                                           #display='inline-block',
                                                           verticalAlign="middle"
                                                        )
                                                    ),
                                                html.Img(id='imageit2', style={'width': '600px'})
                                            ],
                                        ),
                                ],
                                
                            ),
                            dfx.Row(
                                id='row3-1-2',
                                children=[
                                    dfx.Col(
                                        id='col3-2-1',
                                            xs=6,
                                            lg=6,
                                            children=[
                                                html.H3('Location 3'),
                                                    dcc.Dropdown(
                                                        id='image-dropdownIT3',
                                                        options=[{'label': i, 'value': i} for i in list_of_images_italy],
                                                        placeholder="Select Country",
                                                        value=list_of_images_italy[2],
                                                        style=dict(
                                                           width='90%',
                                                           #display='inline-block',
                                                           verticalAlign="middle"
                                                        )
                                                    ),
                                                html.Img(id='imageit3', style={'width': '600px'})
                                            ],
                                        ),
                                    dfx.Col(
                                        id='col3-2-2',
                                            xs=6,
                                            lg=6,
                                            children=[
                                                html.H3('Location 4'),
                                                    dcc.Dropdown(
                                                        id='image-dropdownIT4',
                                                        options=[{'label': i, 'value': i} for i in list_of_images_italy],
                                                        placeholder="Select Country",
                                                        value=list_of_images_italy[3],
                                                        style=dict(
                                                           width='90%',
                                                           #display='inline-block',
                                                           verticalAlign="middle"
                                                        )
                                                    ),
                                                html.Img(id='imageit4', style={'width': '600px'})
                                            ],
                                        ),
                                ],
                                
                            ),
                            dfx.Row(
                                id='row3-1-3',
                                children=[
                                    dfx.Col(
                                        id='col3-3-1',
                                            xs=6,
                                            lg=6,
                                            children=[
                                                html.H3('Location 5'),
                                                    dcc.Dropdown(
                                                        id='image-dropdownIT5',
                                                        options=[{'label': i, 'value': i} for i in list_of_images_italy],
                                                        placeholder="Select Country",
                                                        value=list_of_images_italy[4],
                                                        style=dict(
                                                           width='90%',
                                                           #display='inline-block',
                                                           verticalAlign="middle"
                                                        )
                                                    ),
                                                html.Img(id='imageit5', style={'width': '600px'})
                                            ],
                                        ),
                                    dfx.Col(
                                        id='col3-3-2',
                                            xs=6,
                                            lg=6,
                                            children=[
                                                html.H3('Location 6'),
                                                    dcc.Dropdown(
                                                        id='image-dropdownIT6',
                                                        options=[{'label': i, 'value': i} for i in list_of_images_italy],
                                                        placeholder="Select Country",
                                                        value=list_of_images_italy[5],
                                                        style=dict(
                                                           width='90%',
                                                           #display='inline-block',
                                                           verticalAlign="middle"
                                                        )
                                                    ),
                                                html.Img(id='imageit6', style={'width': '600px'})
                                            ],
                                        ),
                                ],
                                
                            ),

                        ],

                    ),
                ]
            ),
            dcc.Tab(
                label='CANADA',
                value='tab-5',
                style=tab_style,
                selected_style=tab_selected_style,
                children=[
                    dfx.Grid(
                        children=[
                            dfx.Row(
                                id='row4-1-1',
                                children=[
                                    dfx.Col(
                                        id='col4-1-1',
                                            xs=6,
                                            lg=6,
                                            children=[
                                                html.H3('Location 1'),
                                                    dcc.Dropdown(
                                                        id='image-dropdownCA1',
                                                        options=[{'label': i, 'value': i} for i in list_of_images_canada],
                                                        placeholder="Select Country",
                                                        value=list_of_images_canada[0],
                                                        style=dict(
                                                           width='90%',
                                                           #display='inline-block',
                                                           verticalAlign="middle"
                                                        )
                                                    ),
                                                html.Img(id='imageca1', style={'width': '600px'})
                                            ],
                                        ),
                                    dfx.Col(
                                        id='col4-1-2',
                                            xs=6,
                                            lg=6,
                                            children=[
                                                html.H3('Location 2'),
                                                    dcc.Dropdown(
                                                        id='image-dropdownCA2',
                                                        options=[{'label': i, 'value': i} for i in list_of_images_canada],
                                                        placeholder="Select Country",
                                                        value=list_of_images_canada[1],
                                                        style=dict(
                                                           width='90%',
                                                           #display='inline-block',
                                                           verticalAlign="middle"
                                                        )
                                                    ),
                                                html.Img(id='imageca2', style={'width': '600px'})
                                            ],
                                        ),
                                ],
                                
                            ),
                            dfx.Row(
                                id='row4-1-2',
                                children=[
                                    dfx.Col(
                                        id='col4-2-1',
                                            xs=6,
                                            lg=6,
                                            children=[
                                                html.H3('Location 3'),
                                                    dcc.Dropdown(
                                                        id='image-dropdownCA3',
                                                        options=[{'label': i, 'value': i} for i in list_of_images_canada],
                                                        placeholder="Select Country",
                                                        value=list_of_images_canada[2],
                                                        style=dict(
                                                           width='90%',
                                                           #display='inline-block',
                                                           verticalAlign="middle"
                                                        )
                                                    ),
                                                html.Img(id='imageca3', style={'width': '600px'})
                                            ],
                                        ),
                                    dfx.Col(
                                        id='col4-2-2',
                                            xs=6,
                                            lg=6,
                                            children=[
                                                html.H3('Location 4'),
                                                    dcc.Dropdown(
                                                        id='image-dropdownCA4',
                                                        options=[{'label': i, 'value': i} for i in list_of_images_canada],
                                                        placeholder="Select Country",
                                                        value=list_of_images_canada[3],
                                                        style=dict(
                                                           width='90%',
                                                           #display='inline-block',
                                                           verticalAlign="middle"
                                                        )
                                                    ),
                                                html.Img(id='imageca4', style={'width': '600px'})
                                            ],
                                        ),
                                ],
                                
                            ),
                            dfx.Row(
                                id='row4-1-3',
                                children=[
                                    dfx.Col(
                                        id='col4-3-1',
                                            xs=6,
                                            lg=6,
                                            children=[
                                                html.H3('Location 5'),
                                                    dcc.Dropdown(
                                                        id='image-dropdownCA5',
                                                        options=[{'label': i, 'value': i} for i in list_of_images_canada],
                                                        placeholder="Select Country",
                                                        value=list_of_images_canada[4],
                                                        style=dict(
                                                           width='90%',
                                                           #display='inline-block',
                                                           verticalAlign="middle"
                                                        )
                                                    ),
                                                html.Img(id='imageca5', style={'width': '600px'})
                                            ],
                                        ),
                                    dfx.Col(
                                        id='col4-3-2',
                                            xs=6,
                                            lg=6,
                                            children=[
                                                html.H3('Location 6'),
                                                    dcc.Dropdown(
                                                        id='image-dropdownCA6',
                                                        options=[{'label': i, 'value': i} for i in list_of_images_canada],
                                                        placeholder="Select Country",
                                                        value=list_of_images_canada[4],
                                                        style=dict(
                                                           width='90%',
                                                           #display='inline-block',
                                                           verticalAlign="middle"
                                                        )
                                                    ),
                                                html.Img(id='imageca6', style={'width': '600px'})
                                            ],
                                        ),
                                ],
                                
                            ),

                        ],

                    ),
                ]
            ),
            dcc.Tab(
                label='SOUTH AMERICA',
                value='tab-6',
                style=tab_style,
                selected_style=tab_selected_style,
                children=[
                    dfx.Grid(
                        children=[
                            dfx.Row(
                                id='row5-1-1',
                                children=[
                                    dfx.Col(
                                        id='col5-1-1',
                                            xs=6,
                                            lg=6,
                                            children=[
                                                html.H3('Location 1'),
                                                    dcc.Dropdown(
                                                        id='image-dropdownSA1',
                                                        options=[{'label': i, 'value': i} for i in list_of_images_s_america],
                                                        placeholder="Select Country",
                                                        value=list_of_images_s_america[0],
                                                        style=dict(
                                                           width='90%',
                                                           #display='inline-block',
                                                           verticalAlign="middle"
                                                        )
                                                    ),
                                                html.Img(id='imagesa1', style={'width': '600px'})
                                            ],
                                        ),
                                    dfx.Col(
                                        id='col5-1-2',
                                            xs=6,
                                            lg=6,
                                            children=[
                                                html.H3('Location 2'),
                                                    dcc.Dropdown(
                                                        id='image-dropdownSA2',
                                                        options=[{'label': i, 'value': i} for i in list_of_images_s_america],
                                                        placeholder="Select Country",
                                                        value=list_of_images_s_america[1],
                                                        style=dict(
                                                           width='90%',
                                                           #display='inline-block',
                                                           verticalAlign="middle"
                                                        )
                                                    ),
                                                html.Img(id='imagesa2', style={'width': '600px'})
                                            ],
                                        ),
                                ],
                                
                            ),
                            dfx.Row(
                                id='row5-1-2',
                                children=[
                                    dfx.Col(
                                        id='col5-2-1',
                                            xs=6,
                                            lg=6,
                                            children=[
                                                html.H3('Location 3'),
                                                    dcc.Dropdown(
                                                        id='image-dropdownSA3',
                                                        options=[{'label': i, 'value': i} for i in list_of_images_s_america],
                                                        placeholder="Select Country",
                                                        value=list_of_images_s_america[2],
                                                        style=dict(
                                                           width='90%',
                                                           #display='inline-block',
                                                           verticalAlign="middle"
                                                        )
                                                    ),
                                                html.Img(id='imagesa3', style={'width': '600px'})
                                            ],
                                        ),
                                    dfx.Col(
                                        id='col5-2-2',
                                            xs=6,
                                            lg=6,
                                            children=[
                                                html.H3('Location 4'),
                                                    dcc.Dropdown(
                                                        id='image-dropdownSA4',
                                                        options=[{'label': i, 'value': i} for i in list_of_images_s_america],
                                                        placeholder="Select Country",
                                                        value=list_of_images_s_america[3],
                                                        style=dict(
                                                           width='90%',
                                                           #display='inline-block',
                                                           verticalAlign="middle"
                                                        )
                                                    ),
                                                html.Img(id='imagesa4', style={'width': '600px'})
                                            ],
                                        ),
                                ],
                                
                            ),
                            dfx.Row(
                                id='row5-1-3',
                                children=[
                                    dfx.Col(
                                        id='col5-3-1',
                                            xs=6,
                                            lg=6,
                                            children=[
                                                html.H3('Location 5'),
                                                    dcc.Dropdown(
                                                        id='image-dropdownSA5',
                                                        options=[{'label': i, 'value': i} for i in list_of_images_s_america],
                                                        placeholder="Select Country",
                                                        value=list_of_images_s_america[4],
                                                        style=dict(
                                                           width='90%',
                                                           #display='inline-block',
                                                           verticalAlign="middle"
                                                        )
                                                    ),
                                                html.Img(id='imagesa5', style={'width': '600px'})
                                            ],
                                        ),
                                    dfx.Col(
                                        id='col5-3-2',
                                            xs=6,
                                            lg=6,
                                            children=[
                                                html.H3('Location 6'),
                                                    dcc.Dropdown(
                                                        id='image-dropdownSA6',
                                                        options=[{'label': i, 'value': i} for i in list_of_images_s_america],
                                                        placeholder="Select Country",
                                                        value=list_of_images_s_america[5],
                                                        style=dict(
                                                           width='90%',
                                                           #display='inline-block',
                                                           verticalAlign="middle"
                                                        )
                                                    ),
                                                html.Img(id='imagesa6', style={'width': '600px'})
                                            ],
                                        ),
                                ],
                                
                            ),

                        ],

                    ),
                ]
            ),
        ],
        style=tabs_styles,

    ),
    html.Div(id='tabs-content-inline') 
])



 #callbacks
 #WORLD
@app.callback(
    dash.dependencies.Output('imageworld1', 'src'),
    [dash.dependencies.Input('image-dropdownWorld1', 'value')]
)
def update_image_srcWorld1(value):
    return static_image_route_world + value

@app.callback(
    dash.dependencies.Output('imageworld2', 'src'),
    [dash.dependencies.Input('image-dropdownWorld2', 'value')]
)
def update_image_srcWorld2(value):
    return static_image_route_world + value

@app.callback(
    dash.dependencies.Output('imageworld3', 'src'),
    [dash.dependencies.Input('image-dropdownWorld3', 'value')]
)
def update_image_srcWorld3(value):
    return static_image_route_world + value

@app.callback(
    dash.dependencies.Output('imageworld4', 'src'),
    [dash.dependencies.Input('image-dropdownWorld4', 'value')]
)
def update_image_srcWorld4(value):
    return static_image_route_world + value

@app.callback(
    dash.dependencies.Output('imageworld5', 'src'),
    [dash.dependencies.Input('image-dropdownWorld5', 'value')]
)
def update_image_srcWorld5(value):
    return static_image_route_world + value

@app.callback(
    dash.dependencies.Output('imageworld6', 'src'),
    [dash.dependencies.Input('image-dropdownWorld6', 'value')]
)
def update_image_srcWorld6(value):
    return static_image_route_world + value

#US
@app.callback(
    dash.dependencies.Output('imageus1', 'src'),
    [dash.dependencies.Input('image-dropdownUS1', 'value')]
)
def update_image_srcUS1(value):
    return static_image_route_us + value

@app.callback(
    dash.dependencies.Output('imageus2', 'src'),
    [dash.dependencies.Input('image-dropdownUS2', 'value')]
)
def update_image_srcUS2(value):
    return static_image_route_us + value

@app.callback(
    dash.dependencies.Output('imageus3', 'src'),
    [dash.dependencies.Input('image-dropdownUS3', 'value')]
)
def update_image_srcUS3(value):
    return static_image_route_us + value

@app.callback(
    dash.dependencies.Output('imageus4', 'src'),
    [dash.dependencies.Input('image-dropdownUS4', 'value')]
)
def update_image_srcUS4(value):
    return static_image_route_us + value

@app.callback(
    dash.dependencies.Output('imageus5', 'src'),
    [dash.dependencies.Input('image-dropdownUS5', 'value')]
)
def update_image_srcUS5(value):
    return static_image_route_us + value

@app.callback(
    dash.dependencies.Output('imageus6', 'src'),
    [dash.dependencies.Input('image-dropdownUS6', 'value')]
)
def update_image_srcUS6(value):
    return static_image_route_us + value

#Italy
@app.callback(
    dash.dependencies.Output('imageit1', 'src'),
    [dash.dependencies.Input('image-dropdownIT1', 'value')]
)
def update_image_srcIT1(value):
    return static_image_route_italy + value

@app.callback(
    dash.dependencies.Output('imageit2', 'src'),
    [dash.dependencies.Input('image-dropdownIT2', 'value')]
)
def update_image_srcIT2(value):
    return static_image_route_italy + value

@app.callback(
    dash.dependencies.Output('imageit3', 'src'),
    [dash.dependencies.Input('image-dropdownIT3', 'value')]
)
def update_image_srcIT3(value):
    return static_image_route_italy + value

@app.callback(
    dash.dependencies.Output('imageit4', 'src'),
    [dash.dependencies.Input('image-dropdownIT4', 'value')]
)
def update_image_srcIT4(value):
    return static_image_route_italy + value

@app.callback(
    dash.dependencies.Output('imageit5', 'src'),
    [dash.dependencies.Input('image-dropdownIT5', 'value')]
)
def update_image_srcIT5(value):
    return static_image_route_italy + value

@app.callback(
    dash.dependencies.Output('imageit6', 'src'),
    [dash.dependencies.Input('image-dropdownIT6', 'value')]
)
def update_image_srcIT6(value):
    return static_image_route_italy + value


#Canada
@app.callback(
    dash.dependencies.Output('imageca1', 'src'),
    [dash.dependencies.Input('image-dropdownCA1', 'value')]
)
def update_image_srcCA1(value):
    return static_image_route_canada + value

@app.callback(
    dash.dependencies.Output('imageca2', 'src'),
    [dash.dependencies.Input('image-dropdownCA2', 'value')]
)
def update_image_srcCA2(value):
    return static_image_route_canada + value

@app.callback(
    dash.dependencies.Output('imageca3', 'src'),
    [dash.dependencies.Input('image-dropdownCA3', 'value')]
)
def update_image_srcCA3(value):
    return static_image_route_canada + value

@app.callback(
    dash.dependencies.Output('imageca4', 'src'),
    [dash.dependencies.Input('image-dropdownCA4', 'value')]
)
def update_image_srcCA4(value):
    return static_image_route_canada + value

@app.callback(
    dash.dependencies.Output('imageca5', 'src'),
    [dash.dependencies.Input('image-dropdownCA5', 'value')]
)
def update_image_srcCA5(value):
    return static_image_route_canada + value

@app.callback(
    dash.dependencies.Output('imageca6', 'src'),
    [dash.dependencies.Input('image-dropdownCA6', 'value')]
)
def update_image_srcCA6(value):
    return static_image_route_canada + value


#South America

@app.callback(
    dash.dependencies.Output('imagesa1', 'src'),
    [dash.dependencies.Input('image-dropdownSA1', 'value')]
)
def update_image_srcSA1(value):
    return static_image_route_s_america + value

@app.callback(
    dash.dependencies.Output('imagesa2', 'src'),
    [dash.dependencies.Input('image-dropdownSA2', 'value')]
)
def update_image_srcSA2(value):
    return static_image_route_s_america + value

@app.callback(
    dash.dependencies.Output('imagesa3', 'src'),
    [dash.dependencies.Input('image-dropdownSA3', 'value')]
)
def update_image_srcSA3(value):
    return static_image_route_s_america + value

@app.callback(
    dash.dependencies.Output('imagesa4', 'src'),
    [dash.dependencies.Input('image-dropdownSA4', 'value')]
)
def update_image_srcSA4(value):
    return static_image_route_s_america + value

@app.callback(
    dash.dependencies.Output('imagesa5', 'src'),
    [dash.dependencies.Input('image-dropdownSA5', 'value')]
)
def update_image_srcSA5(value):
    return static_image_route_s_america + value

@app.callback(
    dash.dependencies.Output('imagesa6', 'src'),
    [dash.dependencies.Input('image-dropdownSA6', 'value')]
)
def update_image_srcSA6(value):
    return static_image_route_s_america + value

# Add a static image route that serves images from desktop
# Be *very* careful here - you don't want to serve arbitrary files
# from your computer or server
@app.server.route('{}<image_path>.png'.format(static_image_route_world))
def serve_imageWorld(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_world:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_world, image_name)


@app.server.route('{}<image_path>.png'.format(static_image_route_us))
def serve_imageUS(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_us:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_us, image_name)

@app.server.route('{}<image_path>.png'.format(static_image_route_italy))
def serve_imageIT(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_italy:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_italy, image_name)    

@app.server.route('{}<image_path>.png'.format(static_image_route_canada))
def serve_imageCA(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_canada:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_canada, image_name)

@app.server.route('{}<image_path>.png'.format(static_image_route_s_america))
def serve_imageSA(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_s_america:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_s_america, image_name)

if __name__ == '__main__':
    app.run_server(debug=False)