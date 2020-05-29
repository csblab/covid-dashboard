import dash_core_components as dcc
import dash
import dash_core_components as dcc
import dash_flexbox_grid as dfx
import dash_html_components as html
import flask
import glob
import os
import pathlib

from dash.dependencies import Input, Output


scriptdir = pathlib.Path(os.getcwd())  # this notebook

place_holder = scriptdir / 'plots/place_holder.png'

# WORLD

image_directory_first = scriptdir / 'plots/cCdD'
list_of_images_first = sorted([str(f).split('/cCdD/')[1] for f in list(image_directory_first.rglob('*.png'))])
static_image_route_first = '/staticfirst/'

image_directory_second = scriptdir / 'plots/cCd='
list_of_images_second = sorted([str(f).split('/cCd=/')[1] for f in list(image_directory_second.rglob('*.png'))])
static_image_route_second = '/staticsecond/'

image_directory_third = scriptdir / 'plots/cC=='
list_of_images_third = sorted([str(f).split('/cC==/')[1] for f in list(image_directory_third.rglob('*.png'))])
static_image_route_third = '/staticthird/'

image_directory_fourth = scriptdir / 'plots/cC=D'
list_of_images_fourth = sorted([str(f).split('/cC=D/')[1] for f in list(image_directory_fourth.rglob('*.png'))])
static_image_route_fourth = '/staticfourth/'

image_directory_fifth = scriptdir / 'plots/c=dD'
list_of_images_fifth = sorted([str(f).split('/c=dD/')[1] for f in list(image_directory_fifth.rglob('*.png'))])
static_image_route_fifth = '/staticfifth/'

image_directory_sixth = scriptdir / 'plots/c==D'
list_of_images_sixth = sorted([str(f).split('/c==D/')[1] for f in list(image_directory_sixth.rglob('*.png'))])
static_image_route_sixth = '/staticsixth/'

image_directory_seventh = scriptdir / 'plots/c=d='
list_of_images_seventh = sorted([str(f).split('/c=d=/')[1] for f in list(image_directory_seventh.rglob('*.png'))])
static_image_route_seventh = '/staticseventh/'

image_directory_eigth = scriptdir / 'plots/c==='
list_of_images_eigth = sorted([str(f).split('/c===/')[1] for f in list(image_directory_eigth.rglob('*.png'))])
static_image_route_eigth = '/staticeigth/'

image_directory_nineth = scriptdir / 'plots/=CdD'
list_of_images_nineth = sorted([str(f).split('/=CdD/')[1] for f in list(image_directory_nineth.rglob('*.png'))])
static_image_route_nineth = '/staticnineth/'

image_directory_tenth = scriptdir / 'plots/=Cd=/'
list_of_images_tenth = sorted([str(f).split('/=Cd=/')[1] for f in list(image_directory_tenth.rglob('*.png'))])
static_image_route_tenth = '/statictenth/'

image_directory_eleventh = scriptdir / 'plots/=C=D'
list_of_images_eleventh = sorted([str(f).split('/=C=D/')[1] for f in list(image_directory_eleventh.rglob('*.png'))])
static_image_route_eleventh = '/staticeleventh/'

image_directory_twelfth = scriptdir / 'plots/=C=='
list_of_images_twelfth = sorted([str(f).split('/=C==/')[1] for f in list(image_directory_twelfth.rglob('*.png'))])
static_image_route_twelfth = '/statictwelfth/'

image_directory_thirteenth = scriptdir / 'plots/==dD'
list_of_images_thirteenth = sorted([str(f).split('/==dD/')[1] for f in list(image_directory_thirteenth.rglob('*.png'))])
static_image_route_thirteenth = '/staticthirteenth/'

image_directory_fourteenth = scriptdir / 'plots/===D'
list_of_images_fourteenth = sorted([str(f).split('/===D/')[1] for f in list(image_directory_fourteenth.rglob('*.png'))])
static_image_route_fourteenth = '/staticfourteenth/'

image_directory_fifteenth = scriptdir / 'plots/==d='
list_of_images_fifteenth = sorted([str(f).split('/==d=/')[1] for f in list(image_directory_fifteenth.rglob('*.png'))])
static_image_route_fifteenth = '/staticfifteenth/'

image_directory_sixteenth = scriptdir / 'plots/===='
list_of_images_sixteenth = sorted([str(f).split('/====/')[1] for f in list(image_directory_sixteenth.rglob('*.png'))])
static_image_route_sixteenth = '/staticsixteenth/'

# US

image_directory_first_us = scriptdir / 'plots/us/cCdD'
list_of_images_first_us = sorted([str(f).split('/cCdD/')[1] for f in list(image_directory_first_us.rglob('*.png'))])
static_image_route_first_us = '/staticfirstus/'

image_directory_second_us = scriptdir / 'plots/us/cCd='
list_of_images_second_us = sorted([str(f).split('/cCd=/')[1] for f in list(image_directory_second_us.rglob('*.png'))])
static_image_route_second_us = '/staticsecondus/'

image_directory_third_us = scriptdir / 'plots/us/cC=='
list_of_images_third_us = sorted([str(f).split('/cC==/')[1] for f in list(image_directory_third_us.rglob('*.png'))])
static_image_route_third_us = '/staticthirdus/'

image_directory_fourth_us = scriptdir / 'plots/us/cC=D'
list_of_images_fourth_us = sorted([str(f).split('/cC=D/')[1] for f in list(image_directory_fourth_us.rglob('*.png'))])
static_image_route_fourth_us = '/staticfourthus/'

image_directory_fifth_us = scriptdir / 'plots/us/c=dD'
list_of_images_fifth_us = sorted([str(f).split('/c=dD/')[1] for f in list(image_directory_fifth_us.rglob('*.png'))])
static_image_route_fifth_us = '/staticfifthus/'

image_directory_sixth_us = scriptdir / 'plots/us/c==D'
list_of_images_sixth_us = sorted([str(f).split('/c==D/')[1] for f in list(image_directory_sixth_us.rglob('*.png'))])
static_image_route_sixth_us = '/staticsixthus/'

image_directory_seventh_us = scriptdir / 'plots/us/c=d='
list_of_images_seventh_us = sorted([str(f).split('/c=d=/')[1] for f in list(image_directory_seventh_us.rglob('*.png'))])
static_image_route_seventh_us = '/staticseventhus/'

image_directory_eigth_us = scriptdir / 'plots/us/c==='
list_of_images_eigth_us = sorted([str(f).split('/c===/')[1] for f in list(image_directory_eigth_us.rglob('*.png'))])
static_image_route_eigth_us = '/staticeigthus/'

image_directory_nineth_us = scriptdir / 'plots/us/=CdD'
list_of_images_nineth_us = sorted([str(f).split('/=CdD/')[1] for f in list(image_directory_nineth_us.rglob('*.png'))])
static_image_route_nineth_us = '/staticninethus/'

image_directory_tenth_us = scriptdir / 'plots/us/=Cd=/'
list_of_images_tenth_us = sorted([str(f).split('/=Cd=/')[1] for f in list(image_directory_tenth_us.rglob('*.png'))])
static_image_route_tenth_us = '/statictenthus/'

image_directory_eleventh_us = scriptdir / 'plots/us/=C=D'
list_of_images_eleventh_us = sorted([str(f).split('/=C=D/')[1] for f in list(image_directory_eleventh_us.rglob('*.png'))])
static_image_route_eleventh_us = '/staticeleventhus/'

image_directory_twelfth_us = scriptdir / 'plots/us/=C=='
list_of_images_twelfth_us = sorted([str(f).split('/=C==/')[1] for f in list(image_directory_twelfth_us.rglob('*.png'))])
static_image_route_twelfth_us = '/statictwelfthus/'

image_directory_thirteenth_us = scriptdir / 'plots/us/==dD'
list_of_images_thirteenth_us = sorted([str(f).split('/==dD/')[1] for f in list(image_directory_thirteenth_us.rglob('*.png'))])
static_image_route_thirteenth_us = '/staticthirteenthus/'

image_directory_fourteenth_us = scriptdir / 'plots/us/===D'
list_of_images_fourteenth_us = sorted([str(f).split('/===D/')[1] for f in list(image_directory_fourteenth_us.rglob('*.png'))])
static_image_route_fourteenth_us  = '/staticfourteenthus/'

image_directory_fifteenth_us = scriptdir / 'plots/us/==d='
list_of_images_fifteenth_us = sorted([str(f).split('/==d=/')[1] for f in list(image_directory_fifteenth_us.rglob('*.png'))])
static_image_route_fifteenth_us = '/staticfifteenthus/'

image_directory_sixteenth_us = scriptdir / 'plots/us/===='
list_of_images_sixteenth_us = sorted([str(f).split('/====/')[1] for f in list(image_directory_sixteenth_us.rglob('*.png'))])
static_image_route_sixteenth_us = '/staticsixteenthus/'


app = dash.Dash(__name__)
server = app.server #for server deployment
app.scripts.config.serve_locally = True

tabs_styles = {
    'height': '44px'
}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold'
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#248C92',
    'color': 'white',
    'padding': '6px'
}


app.layout = html.Div([
    dcc.Tabs(
        id="tabs-styled-with-inline",
        value='tab-1',
        children=[
            dcc.Tab(
                label='WORLD',
                value='tab-1',
                style=tab_style,
                selected_style=tab_selected_style,
                children=[
                    dfx.Grid(
                            id='grid',
                            fluid=True,
                            children=[
                                    dfx.Row(
                                        id='row1',
                                        children=[
                                                dfx.Col(
                                                    id='col1-1',
                                                    xs=6,
                                                    lg=6,
                                                    children=[
                                                            html.H3('cCdD'),
                                                            dcc.Dropdown(
                                                                id='image-dropdownFirst',
                                                                options=[{'label': i, 'value': i} for i in list_of_images_first],
                                                                placeholder="Select Country",
                                                                #value=list_of_images_first[0],
                                                                style=dict(
                                                                     width='90%',
                                                                     #display='inline-block',
                                                                     verticalAlign="middle"
                                                                )
                                                            ),
                                                            html.Img(id='imagefirst', style={'width': '600px'})
                                                    ],
                                                ),
                                                dfx.Col(
                                                    id='col1-2',
                                                    xs=6,
                                                    lg=6,
                                                    children=[
                                                            html.H3('cCd='),
                                                            dcc.Dropdown(
                                                                id='image-dropdownSecond',
                                                                options=[{'label': i, 'value': i} for i in list_of_images_second],
                                                                placeholder="Select Country",
                                                                #value=list_of_images_second[0],
                                                                style=dict(
                                                                        width='90%',
                                                                        #display='inline-block',
                                                                        verticalAlign = "middle"
                                                                )
                                                            ),
                                                            html.Img(id='imagesecond', style={'width': '600px'})
                                                    ]
                                                ),
                                        ],
                                     ),
                                    dfx.Row(
                                        id='row2',
                                        children=[
                                                dfx.Col(
                                                    id='col2-1',
                                                    xs=6,
                                                    lg=6,
                                                    children=[
                                                            html.H3('cC=='),
                                                            dcc.Dropdown(
                                                                id='image-dropdownThird',
                                                                options=[{'label': i, 'value': i} for i in list_of_images_third],
                                                                placeholder="Select Country",
                                                                #value=list_of_images_third[0],
                                                                style=dict(
                                                                        width='90%',
                                                                        #display='inline-block',
                                                                        verticalAlign = "middle"
                                                                )
                                                            ),
                                                            html.Img(id='imagethird', style={'width': '600px'}),
                                                    ]
                                                ),
                                                dfx.Col(
                                                    id='col2-2',
                                                    xs=6, 
                                                    lg=6, 
                                                    children=[
                                                            html.H3('cC=D'),
                                                            dcc.Dropdown(
                                                                id='image-dropdownFourth',
                                                                options=[{'label': i, 'value': i} for i in list_of_images_fourth],
                                                                placeholder="Select Country",
                                                                #value=list_of_images_fourth[0],
                                                                style=dict(
                                                                        width='90%',
                                                                        #display='inline-block',
                                                                        verticalAlign = "middle"
                                                                )
                                                            ),
                                                            html.Img(id='imagefourth', style={'width': '600px'}),
                                                    ]
                                                ),
                                        ]
                                    ),
                                    dfx.Row(
                                        id='row3',
                                        children=[
                                                dfx.Col(
                                                    id='col3-1',
                                                    xs=6,
                                                    lg=6,
                                                    children=[
                                                            html.H3('c=dD'),
                                                            dcc.Dropdown(
                                                                id='image-dropdownFifth',
                                                                options=[{'label': i, 'value': i} for i in list_of_images_fifth],
                                                                placeholder="Select Country",
                                                                #value=list_of_images_fifth[0],
                                                                style=dict(
                                                                    width='90%',
                                                                    #display='inline-block',
                                                                    verticalAlign = "middle"
                                                                )
                                                            ),
                                                            html.Img(id='imagefifth', style={'width': '600px'}),
                                                    ]
                                                ),
                                                dfx.Col(
                                                    id='col3-2', 
                                                    xs=6, 
                                                    lg=6, 
                                                    children=[
                                                            html.H3('c==D'),
                                                            dcc.Dropdown(
                                                                id='image-dropdownSixth',
                                                                options=[{'label': i, 'value': i} for i in list_of_images_sixth],
                                                                placeholder="Select Country",
                                                                #value=list_of_images_sixth[0],
                                                                style=dict(
                                                                    width='90%',
                                                                    #display='inline-block',
                                                                    verticalAlign = "middle"
                                                                )
                                                            ),
                                                            html.Img(id='imagesixth', style={'width': '600px'}),
                                                    ]
                                                ),
                                        ]
                                    ),
                                    dfx.Row(
                                        id='row4',
                                        children=[
                                                dfx.Col(
                                                    id='col4-1', 
                                                    xs=6, 
                                                    lg=6, 
                                                    children=[
                                                            html.H3('c=d='),
                                                            dcc.Dropdown(
                                                                id='image-dropdownSeventh',
                                                                options=[{'label': i, 'value': i} for i in list_of_images_seventh],
                                                                placeholder="Select Country",
                                                                #value=list_of_images_seventh[0],
                                                                style=dict(
                                                                    width='90%',
                                                                    #display='inline-block',
                                                                    verticalAlign = "middle"
                                                                )
                                                            ),
                                                            html.Img(id='imageseventh', style={'width': '600px'}),
                                                    ]
                                                ), 
                                                dfx.Col(
                                                    id='col4-2', 
                                                    xs=6, 
                                                    lg=6, 
                                                    children=[
                                                            html.H3('c==='),
                                                            dcc.Dropdown(
                                                                id='image-dropdownEigth',
                                                                options=[{'label': i, 'value': i} for i in list_of_images_eigth],
                                                                placeholder="Select Country",
                                                                #value=list_of_images_eigth[0],
                                                                style=dict(
                                                                    width='90%',
                                                                    #display='inline-block',
                                                                    verticalAlign = "middle"
                                                                )
                                                            ),
                                                            html.Img(id='imageeigth', style={'width': '600px'}),
                                                    ]
                                                ),
                                        ]
                                    ),
                                    dfx.Row(
                                        id='row5', 
                                        children=[ 
                                                dfx.Col(
                                                    id='col5-1', 
                                                    xs=6, 
                                                    lg=6, 
                                                    children=[
                                                            html.H3('=CdD'),
                                                            dcc.Dropdown(
                                                                id='image-dropdownNineth',
                                                                options=[{'label': i, 'value': i} for i in list_of_images_nineth],
                                                                placeholder="Select Country",
                                                                #value=list_of_images_nineth[0],
                                                                style=dict(
                                                                    width='90%',
                                                                    #display='inline-block',
                                                                    verticalAlign = "middle"
                                                                )
                                                            ),
                                                            html.Img(id='imagenineth', style={'width': '600px'}),
                                                    ]
                                                ),
                                                dfx.Col(
                                                    id='col5-2', 
                                                    xs=6, 
                                                    lg=6, 
                                                    children=[
                                                            html.H3('=Cd='),
                                                            dcc.Dropdown(
                                                                id='image-dropdownTenth',
                                                                options=[{'label': i, 'value': i} for i in list_of_images_tenth],
                                                                placeholder="Select Country",
                                                                #value=list_of_images_tenth[0],
                                                                style=dict(
                                                                    width='90%',
                                                                    #display='inline-block',
                                                                    verticalAlign = "middle"
                                                                )
                                                            ),
                                                            html.Img(id='imagetenth', style={'width': '600px'}),
                                                    ]
                                                ),
                                        ]
                                    ),
                                    dfx.Row(
                                        id='row6', 
                                        children=[ 
                                                dfx.Col(
                                                    id='col6-1', 
                                                    xs=6, 
                                                    lg=6, 
                                                    children=[
                                                            html.H3('=C=D'),
                                                            dcc.Dropdown(
                                                                id='image-dropdownEleventh',
                                                                options=[{'label': i, 'value': i} for i in list_of_images_eleventh],
                                                                placeholder="Select Country",
                                                                #value=list_of_images_eleventh[0],
                                                                style=dict(
                                                                    width='90%',
                                                                    #display='inline-block',
                                                                    verticalAlign = "middle"
                                                                )
                                                            ),
                                                            html.Img(id='imageeleventh', style={'width': '600px'}),
                                                    ]
                                                ),
                                                dfx.Col(
                                                    id='col6-2', 
                                                    xs=6, 
                                                    lg=6, 
                                                    children=[
                                                            html.H3('=C=='),
                                                            dcc.Dropdown(
                                                                id='image-dropdownTwelfth',
                                                                options=[{'label': i, 'value': i} for i in list_of_images_twelfth],
                                                                placeholder="Select Country",
                                                                #value=list_of_images_twelfth[0],
                                                                style=dict(
                                                                    width='90%',
                                                                    #display='inline-block',
                                                                    verticalAlign = "middle"
                                                                )
                                                            ),
                                                            html.Img(id='imagetwelfth', style={'width': '600px'}),
                                                    ]
                                                ),
                                        ]
                                    ),
                                    dfx.Row(
                                        id='row7', 
                                        children=[ 
                                                dfx.Col(
                                                    id='col7-1', 
                                                    xs=6, 
                                                    lg=6, 
                                                    children=[
                                                            html.H3('==dD'),
                                                            dcc.Dropdown(
                                                                id='image-dropdownThirteenth',
                                                                options=[{'label': i, 'value': i} for i in list_of_images_thirteenth],
                                                                placeholder="Select Country",
                                                                #value=list_of_images_thirteenth[0],
                                                                style=dict(
                                                                    width='90%',
                                                                    #display='inline-block',
                                                                    verticalAlign = "middle"
                                                                )
                                                            ),
                                                            html.Img(id='imagethirteenth', style={'width': '600px'}),
                                                    ]
                                                ), 
                                                dfx.Col(
                                                    id='col7-2',
                                                    xs=6, 
                                                    lg=6, 
                                                    children=[
                                                            html.H3('===D'),
                                                            dcc.Dropdown(
                                                                id='image-dropdownFourteenth',
                                                                options=[{'label': i, 'value': i} for i in list_of_images_fourteenth],
                                                                placeholder="Select Country",
                                                                #value=list_of_images_fourteenth[0],
                                                                style=dict(
                                                                    width='90%',
                                                                    #display='inline-block',
                                                                    verticalAlign = "middle"
                                                                )
                                                            ),
                                                            html.Img(id='imagefourteenth', style={'width': '600px'}),
                                                    ]
                                                ),
                                        ]
                                    ),
                                    dfx.Row(
                                        id='row8',
                                        children=[
                                                dfx.Col(
                                                    id='col8-1',
                                                    xs=6,
                                                    lg=6,
                                                    children=[
                                                            html.H3('==d='),
                                                            dcc.Dropdown(
                                                                id='image-dropdownFifteenth',
                                                                options=[{'label': i, 'value': i} for i in list_of_images_fifteenth],
                                                                placeholder="Select Country",
                                                                #value=list_of_images_fifteenth[0],
                                                                style=dict(
                                                                    width='90%',
                                                                    #display='inline-block',
                                                                    verticalAlign = "middle"
                                                                )
                                                            ),
                                                            html.Img(id='imagefifteenth', style={'width': '600px'}),
                                                    ]
                                                ),
                                                dfx.Col(
                                                    id='col8-2',
                                                    xs=6, 
                                                    lg=6, 
                                                    children=[
                                                            html.H3('===='),
                                                            dcc.Dropdown(
                                                                id='image-dropdownSixteenth',
                                                                options=[{'label': i, 'value': i} for i in list_of_images_sixteenth],
                                                                placeholder="Select Country",
                                                                #value=list_of_images_sixteenth[0],
                                                                style=dict(
                                                                    width='90%',
                                                                    #display='inline-block',
                                                                    verticalAlign = "middle"
                                                                )
                                                            ),
                                                            html.Img(id='imagesixteenth', style={'width': '600px'}),
                                                    ]
                                                ),
                                        ]
                                    ),
                             ]
                     ),

                ],
            ),
            dcc.Tab(
                label='US',
                value='tab-2',
                style=tab_style,
                selected_style=tab_selected_style,
                children=[
                    dfx.Grid(
                        id='gridus', 
                        fluid=True, 
                        children=[ 
                                dfx.Row(
                                    id='row1us',
                                    children=[
                                            dfx.Col(
                                                id='col1-1us', 
                                                xs=6, 
                                                lg=6, 
                                                children=[
                                                        html.H3('cCdD'),
                                                        dcc.Dropdown(
                                                            id='image-dropdownFirst_us',
                                                            options=[{'label': i, 'value': i} for i in list_of_images_first_us],
                                                            placeholder="Select State",
                                                            #value=list_of_images_first_us[0],
                                                            style=dict(
                                                                width='90%',
                                                                #display='inline-block',
                                                                verticalAlign = "middle"
                                                            )
                                                        ),
                                                        html.Img(id='imagefirst_us', style={'width': '600px'})
                                                ]
                                            ),
                                            dfx.Col(
                                                id='col1-2us', 
                                                xs=6,
                                                lg=6, 
                                                children=[
                                                        html.H3('cCd='),
                                                        dcc.Dropdown(
                                                                id='image-dropdownSecond_us',
                                                                options=[{'label': i, 'value': i} for i in list_of_images_second_us],
                                                                placeholder="Select State",
                                                                #value=list_of_images_second_us[0],
                                                                style=dict(
                                                                    width='90%',
                                                                    #display='inline-block',
                                                                    verticalAlign = "middle"
                                                                )
                                                            ),
                                                        html.Img(id='imagesecond_us', style={'width': '600px'})
                                                ]
                                            ),
                                    ]
                                ),
                                dfx.Row(
                                    id='row2us', 
                                    children=[ 
                                            dfx.Col(
                                                id='col2-1us', 
                                                xs=6, 
                                                lg=6, 
                                                children=[
                                                        html.H3('cC=='),
                                                        dcc.Dropdown(
                                                            id='image-dropdownThird_us',
                                                            options=[{'label': i, 'value': i} for i in list_of_images_third_us],
                                                            placeholder="Select State",
                                                            #value=list_of_images_third_us[0],
                                                            style=dict(
                                                                width='90%',
                                                                #display='inline-block',
                                                                verticalAlign = "middle"
                                                            )
                                                        ),
                                                        html.Img(id='imagethird_us', style={'width': '600px'}),
                                                ]
                                            ), 
                                            dfx.Col(
                                                id='col2-2us', 
                                                xs=6, 
                                                lg=6, 
                                                children=[
                                                        html.H3('cC=D'),
                                                        dcc.Dropdown(
                                                            id='image-dropdownFourth_us',
                                                            options=[{'label': i, 'value': i} for i in list_of_images_fourth_us],
                                                            placeholder="Select State",
                                                            #value=list_of_images_fourth_us[0],
                                                            style=dict(
                                                                width='90%',
                                                                #display='inline-block',
                                                                verticalAlign = "middle"
                                                            )
                                                        ),
                                                        html.Img(id='imagefourth_us', style={'width': '600px'}),
                                                ]
                                            ),
                                    ]
                                ),
                                dfx.Row(
                                    id='row3us', 
                                    children=[ 
                                            dfx.Col(
                                                id='col3-1us', 
                                                xs=6, 
                                                lg=6, 
                                                children=[
                                                        html.H3('c=dD'),
                                                        dcc.Dropdown(
                                                            id='image-dropdownFifth_us',
                                                            options=[{'label': i, 'value': i} for i in list_of_images_fifth_us],
                                                            placeholder="Select State",
                                                            #value=list_of_images_fifth_us[0],
                                                            style=dict(
                                                                width='90%',
                                                                #display='inline-block',
                                                                verticalAlign = "middle"
                                                            )
                                                        ),
                                                        html.Img(id='imagefifth_us', style={'width': '600px'}),
                                                ]
                                            ),
                                            dfx.Col(
                                                id='col3-2us',
                                                xs=6, 
                                                lg=6, 
                                                children=[
                                                        html.H3('c==D'),
                                                        dcc.Dropdown(
                                                            id='image-dropdownSixth_us',
                                                            options=[{'label': i, 'value': i} for i in list_of_images_sixth_us],
                                                            placeholder="Select State",
                                                            #value=list_of_images_sixth_us[0],
                                                            style=dict(
                                                                width='90%',
                                                                #display='inline-block',
                                                                verticalAlign = "middle"
                                                            )
                                                        ),
                                                        html.Img(id='imagesixth_us', style={'width': '600px'}),
                                                ]
                                            ),
                                    ]
                                ),
                                dfx.Row(
                                    id='row4-1us', 
                                    children=[ 
                                            dfx.Col(
                                                id='col4us', 
                                                xs=6, 
                                                lg=6, 
                                                children=[
                                                        html.H3('c=d='),
                                                        dcc.Dropdown(
                                                            id='image-dropdownSeventh_us',
                                                            options=[{'label': i, 'value': i} for i in list_of_images_seventh_us],
                                                            placeholder="Select State",
                                                            #value=list_of_images_seventh_us[0],
                                                            style=dict(
                                                                width='90%',
                                                                #display='inline-block',
                                                                verticalAlign = "middle"
                                                            )
                                                        ),
                                                        html.Img(id='imageseventh_us', style={'width': '600px'}),
                                                ]
                                            ),
                                            dfx.Col(
                                                id='row4-2us', 
                                                xs=6, 
                                                lg=6, 
                                                children=[
                                                        html.H3('c==='),
                                                        dcc.Dropdown(
                                                            id='image-dropdownEigth_us',
                                                            options=[{'label': i, 'value': i} for i in list_of_images_eigth_us],
                                                            placeholder="Select State",
                                                            #value=list_of_images_eigth_us[0],
                                                            style=dict(
                                                                width='90%',
                                                                #display='inline-block',
                                                                verticalAlign = "middle"
                                                            )
                                                        ),
                                                        html.Img(id='imageeigth_us', style={'width': '600px'}),
                                                ]
                                            ),
                                    ]
                                ),
                                dfx.Row(
                                    id='row5us',
                                    children=[
                                            dfx.Col(
                                                id='col5-1us', 
                                                xs=6, 
                                                lg=6, 
                                                children=[
                                                        html.H3('=CdD'),
                                                        dcc.Dropdown(
                                                            id='image-dropdownNineth_us',
                                                            options=[{'label': i, 'value': i} for i in list_of_images_nineth_us],
                                                            placeholder="Select State",
                                                            #value=list_of_images_nineth_us[0],
                                                            style=dict(
                                                                width='90%',
                                                                #display='inline-block',
                                                                verticalAlign = "middle"
                                                            )
                                                        ),
                                                        html.Img(id='imagenineth_us', style={'width': '600px'}),
                                                ]
                                            ),
                                            dfx.Col(
                                                id='col5-2us', 
                                                xs=6, 
                                                lg=6, 
                                                children=[
                                                        html.H3('=Cd='),
                                                        dcc.Dropdown(
                                                            id='image-dropdownTenth_us',
                                                            options=[{'label': i, 'value': i} for i in list_of_images_tenth_us],
                                                            placeholder="Select State",
                                                            #value=list_of_images_tenth_us[0],
                                                            style=dict(
                                                                width='90%',
                                                                #display='inline-block',
                                                                verticalAlign = "middle"
                                                            )
                                                        ),
                                                        html.Img(id='imagetenth_us', style={'width': '600px'}),
                                                ]
                                            ),
                                    ]
                                ), 
                                dfx.Row(
                                    id='row6us', 
                                    children=[ 
                                            dfx.Col(
                                                id='col6-1us', 
                                                xs=6, 
                                                lg=6, 
                                                children=[
                                                        html.H3('=C=D'),
                                                        dcc.Dropdown(
                                                            id='image-dropdownEleventh_us',
                                                            options=[{'label': i, 'value': i} for i in list_of_images_eleventh_us],
                                                            placeholder="Select State",
                                                            #value=list_of_images_eleventh_us[0],
                                                            style=dict(
                                                                width='90%',
                                                                #display='inline-block',
                                                                verticalAlign = "middle"
                                                            )
                                                        ),
                                                        html.Img(id='imageeleventh_us', style={'width': '600px'}),
                                                ]
                                            ), 
                                            dfx.Col(
                                                id='col6-2us', 
                                                xs=6, 
                                                lg=6, 
                                                children=[
                                                        html.H3('=C=='),
                                                        dcc.Dropdown(
                                                            id='image-dropdownTwelfth_us',
                                                            options=[{'label': i, 'value': i} for i in list_of_images_twelfth_us],
                                                            placeholder="Select State",
                                                            #value=list_of_images_twelfth_us[0],
                                                            style=dict(
                                                                width='90%',
                                                                #display='inline-block',
                                                                verticalAlign = "middle"
                                                            )
                                                        ),
                                                        html.Img(id='imagetwelfth_us', style={'width': '600px'}),
                                                ]
                                            ),
                                    ]
                                ),
                                dfx.Row(
                                    id='row7us', 
                                    children=[ 
                                            dfx.Col(
                                                id='col7-1us', 
                                                xs=6, 
                                                lg=6, 
                                                children=[
                                                        html.H3('==dD'),
                                                        dcc.Dropdown(
                                                            id='image-dropdownThirteenth_us',
                                                            options=[{'label': i, 'value': i} for i in list_of_images_thirteenth_us],
                                                            placeholder="Select State",
                                                            #value=list_of_images_thirteenth_us[0],
                                                            style=dict(
                                                                width='90%',
                                                                #display='inline-block',
                                                                verticalAlign = "middle"
                                                            )
                                                        ),
                                                        html.Img(id='imagethirteenth_us', style={'width': '600px'}),
                                                ]
                                            ), 
                                            dfx.Col(
                                                id='col7-2us', 
                                                xs=6, 
                                                lg=6, 
                                                children=[
                                                        html.H3('===D'),
                                                        dcc.Dropdown(
                                                            id='image-dropdownFourteenth_us',
                                                            options=[{'label': i, 'value': i} for i in list_of_images_fourteenth_us],
                                                            placeholder="Select State",
                                                            #value=list_of_images_twelfth_us[0],
                                                            style=dict(
                                                                width='90%',
                                                                #display='inline-block',
                                                                verticalAlign = "middle"
                                                            )
                                                        ),
                                                        html.Img(id='imagefourteenth_us', style={'width': '600px'}),
                                                ]
                                            ),
                                    ]
                                ),
                                dfx.Row(
                                    id='row8us', 
                                    children=[ 
                                            dfx.Col(
                                                id='col8-1us', 
                                                xs=6, 
                                                lg=6, 
                                                children=[
                                                        html.H3('==d='),
                                                        dcc.Dropdown(
                                                            id='image-dropdownFifteenth_us',
                                                            options=[{'label': i, 'value': i} for i in list_of_images_fifteenth_us],
                                                            placeholder="Select State",
                                                            #value=list_of_images_fifteenth_us[0],
                                                            style=dict(
                                                                width='90%',
                                                                #display='inline-block',
                                                                verticalAlign = "middle"
                                                            )
                                                        ),
                                                        html.Img(id='imagefifteenth_us', style={'width': '600px'}),
                                                ]
                                            ), 
                                            dfx.Col(
                                                id='col8-2us', 
                                                xs=6, 
                                                lg=6, 
                                                children=[
                                                        html.H3('===='),
                                                        dcc.Dropdown(
                                                            id='image-dropdownSixteenth_us',
                                                            options=[{'label': i, 'value': i} for i in list_of_images_sixteenth_us],
                                                            placeholder="Select State",
                                                            #value=list_of_images_twelfth_us[0],
                                                            style=dict(
                                                                width='90%',
                                                                #display='inline-block',
                                                                verticalAlign = "middle"
                                                            )
                                                        ),
                                                        html.Img(id='imagesixteenth_us', style={'width': '600px'}),
                                                ]
                                            ),
                                    ]
                                ),
                        ]
                    ),
                ],
            ),
        ],
        style=tabs_styles,
    ),
    html.Div(id='tabs-content-inline')
])

#callbacks

# WORLD
@app.callback(
    dash.dependencies.Output('imagefirst', 'src'),
    [dash.dependencies.Input('image-dropdownFirst', 'value')]
)
def update_image_srcFirst(value):
    if value:
        return static_image_route_first + value


@app.callback(
    dash.dependencies.Output('imagesecond', 'src'),
    [dash.dependencies.Input('image-dropdownSecond', 'value')]
)
def update_image_srcSecond(value):
    if value:
        return static_image_route_second + value

@app.callback(
    dash.dependencies.Output('imagethird', 'src'),
    [dash.dependencies.Input('image-dropdownThird', 'value')]
)
def update_image_srcThird(value):
    if value:
        return static_image_route_third + value

@app.callback(
    dash.dependencies.Output('imagefourth', 'src'),
    [dash.dependencies.Input('image-dropdownFourth', 'value')]
)
def update_image_srcFourth(value):
    if value:
        return static_image_route_fourth + value

@app.callback(
    dash.dependencies.Output('imagefifth', 'src'),
    [dash.dependencies.Input('image-dropdownFifth', 'value')]
)
def update_image_srcFifth(value):
    if value:
        return static_image_route_fifth + value

@app.callback(
    dash.dependencies.Output('imagesixth', 'src'),
    [dash.dependencies.Input('image-dropdownSixth', 'value')]
)
def update_image_srcSixth(value):
    if value:
        return static_image_route_sixth + value


@app.callback(
    dash.dependencies.Output('imageseventh', 'src'),
    [dash.dependencies.Input('image-dropdownSeventh', 'value')]
)
def update_image_srcSeventh(value):
    if value:
        return static_image_route_seventh + value

@app.callback(
    dash.dependencies.Output('imageeigth', 'src'),
    [dash.dependencies.Input('image-dropdownEigth', 'value')]
)
def update_image_srcEight(value):
    if value:
        return static_image_route_eigth + value

@app.callback(
    dash.dependencies.Output('imagenineth', 'src'),
    [dash.dependencies.Input('image-dropdownNineth', 'value')]
)
def update_image_srcNineth(value):
    if value:
         return static_image_route_nineth + value
    
@app.callback(
    dash.dependencies.Output('imagetenth', 'src'),
    [dash.dependencies.Input('image-dropdownTenth', 'value')]
)
def update_image_srcTenth(value):
    if value:
        return static_image_route_tenth + value
    
@app.callback(
    dash.dependencies.Output('imageeleventh', 'src'),
    [dash.dependencies.Input('image-dropdownEleventh', 'value')]
)
def update_image_srcEleventh(value):
    if value:
        return static_image_route_eleventh+ value
    
@app.callback(
    dash.dependencies.Output('imagetwelfth', 'src'),
    [dash.dependencies.Input('image-dropdownTwelfth', 'value')]
)
def update_image_srcTwelve(value):
    if value:
        return static_image_route_twelfth + value

@app.callback(
    dash.dependencies.Output('imagethirteenth', 'src'),
    [dash.dependencies.Input('image-dropdownThirteenth', 'value')]
)
def update_image_srcThirteenth(value):
    if value:
        return static_image_route_thirteenth + value

@app.callback(
    dash.dependencies.Output('imagefourteenth', 'src'),
    [dash.dependencies.Input('image-dropdownFourteenth', 'value')]
)
def update_image_srcFourteenth(value):
    if value:
        return static_image_route_fourteenth + value

@app.callback(
    dash.dependencies.Output('imagefifteenth', 'src'),
    [dash.dependencies.Input('image-dropdownFifteenth', 'value')]
)
def update_image_srcFifteenth(value):
    if value:
        return static_image_route_fifteenth + value

@app.callback(
    dash.dependencies.Output('imagesixteenth', 'src'),
    [dash.dependencies.Input('image-dropdownSixteenth', 'value')]
)
def update_image_srcSixteenth(value):
    if value:
        return static_image_route_sixteenth + value


# US

@app.callback(
    dash.dependencies.Output('imagefirst_us', 'src'),
    [dash.dependencies.Input('image-dropdownFirst_us', 'value')]
)
def update_image_srcFirst_us(value):
    if value:
        return static_image_route_first_us + value


@app.callback(
    dash.dependencies.Output('imagesecond_us', 'src'),
    [dash.dependencies.Input('image-dropdownSecond_us', 'value')]
)
def update_image_srcSecond_us(value):
    if value:
        return static_image_route_second_us + value

@app.callback(
    dash.dependencies.Output('imagethird_us', 'src'),
    [dash.dependencies.Input('image-dropdownThird_us', 'value')]
)
def update_image_srcThird_us(value):
    if value:
        return static_image_route_third_us + value

@app.callback(
    dash.dependencies.Output('imagefourth_us', 'src'),
    [dash.dependencies.Input('image-dropdownFourth_us', 'value')]
)
def update_image_srcFourth_us(value):
    if value:
        return static_image_route_fourth_us + value

@app.callback(
    dash.dependencies.Output('imagefifth_us', 'src'),
    [dash.dependencies.Input('image-dropdownFifth_us', 'value')]
)
def update_image_srcFifth_us(value):
    if value:
        return static_image_route_fifth_us + value

@app.callback(
    dash.dependencies.Output('imagesixth_us', 'src'),
    [dash.dependencies.Input('image-dropdownSixth_us', 'value')]
)
def update_image_srcSixth_us(value):
    if value:
        return static_image_route_sixth_us + value


@app.callback(
    dash.dependencies.Output('imageseventh_us', 'src'),
    [dash.dependencies.Input('image-dropdownSeventh_us', 'value')]
)
def update_image_srcSeventh_us(value):
    if value:
        return static_image_route_seventh_us + value
    
@app.callback(
    dash.dependencies.Output('imageeigth_us', 'src'),
    [dash.dependencies.Input('image-dropdownEigth_us', 'value')]
)
def update_image_srcEight_us(value):
    if value:
        return static_image_route_eigth_us + value
    
@app.callback(
    dash.dependencies.Output('imagenineth_us', 'src'),
    [dash.dependencies.Input('image-dropdownNineth_us', 'value')]
)
def update_image_srcNineth_us(value):
    if value:
        return static_image_route_nineth_us + value
    
@app.callback(
    dash.dependencies.Output('imagetenth_us', 'src'),
    [dash.dependencies.Input('image-dropdownTenth_us', 'value')]
)
def update_image_srcTenth_us(value):
    if value:
        return static_image_route_tenth_us + value
    
@app.callback(
    dash.dependencies.Output('imageeleventh_us', 'src'),
    [dash.dependencies.Input('image-dropdownEleventh_us', 'value')]
)
def update_image_srcEleventh(value):
    if value:
        return static_image_route_eleventh_us + value
    
@app.callback(
    dash.dependencies.Output('imagetwelfth_us', 'src'),
    [dash.dependencies.Input('image-dropdownTwelfth_us', 'value')]
)
def update_image_srcTwelve_us(value):
    if value:
        return static_image_route_twelfth_us + value

@app.callback(
    dash.dependencies.Output('imagethirteenth_us', 'src'),
    [dash.dependencies.Input('image-dropdownThirteenth_us', 'value')]
)
def update_image_srcThirteenth_us(value):
    if value:
       return static_image_route_thirteenth_us + value

@app.callback(
    dash.dependencies.Output('imagefourteenth_us', 'src'),
    [dash.dependencies.Input('image-dropdownFourteenth_us', 'value')]
)
def update_image_srcFourteenth_us(value):
    if value:
        return static_image_route_fourteenth_us + value

@app.callback(
    dash.dependencies.Output('imagefifteenth_us', 'src'),
    [dash.dependencies.Input('image-dropdownFifteenth_us', 'value')]
)
def update_image_srcFifteenth_us(value):
    if value:
        return static_image_route_fifteenth_us + value

@app.callback(
    dash.dependencies.Output('imagesixteenth_us', 'src'),
    [dash.dependencies.Input('image-dropdownSixteenth_us', 'value')]
)
def update_image_srcSixteenth_us(value):
    if value:
        return static_image_route_sixteenth_us + value





# # Add a static image route that serves images from desktop
# # Be *very* careful here - you don't want to serve arbitrary files
# # from your computer or server

# # WORLD
@app.server.route('{}<image_path>.png'.format(static_image_route_first))
def serve_imageFirst(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_first:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_first, image_name)

@app.server.route('{}<image_path>.png'.format(static_image_route_second))
def serve_imageSecond(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_second:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_second, image_name)

@app.server.route('{}<image_path>.png'.format(static_image_route_third))
def serve_imageThird(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_third:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_third, image_name)

@app.server.route('{}<image_path>.png'.format(static_image_route_fourth))
def serve_imageFourth(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_fourth:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_fourth, image_name)

@app.server.route('{}<image_path>.png'.format(static_image_route_fifth))
def serve_imageFifth(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_fifth:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_fifth, image_name)

@app.server.route('{}<image_path>.png'.format(static_image_route_sixth))
def serve_imageSixth(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_sixth:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_sixth, image_name)

@app.server.route('{}<image_path>.png'.format(static_image_route_seventh))
def serve_imageSeventh(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_seventh:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_seventh, image_name)

@app.server.route('{}<image_path>.png'.format(static_image_route_eigth))
def serve_imageEigth(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_eigth:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_eigth, image_name)

@app.server.route('{}<image_path>.png'.format(static_image_route_nineth))
def serve_imageNineth(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_nineth:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_nineth, image_name)

@app.server.route('{}<image_path>.png'.format(static_image_route_tenth))
def serve_imageTenth(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_tenth:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_tenth, image_name)

@app.server.route('{}<image_path>.png'.format(static_image_route_eleventh))
def serve_imageEleventh(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_eleventh:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_eleventh, image_name)

@app.server.route('{}<image_path>.png'.format(static_image_route_twelfth))
def serve_imageNTwelvth(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_twelfth:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_twelfth, image_name)

@app.server.route('{}<image_path>.png'.format(static_image_route_thirteenth))
def serve_imageThirteenth(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_thirteenth:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_thirteenth, image_name)

@app.server.route('{}<image_path>.png'.format(static_image_route_fourteenth))
def serve_imageFourteenth(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_fourteenth:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_fourteenth, image_name)

@app.server.route('{}<image_path>.png'.format(static_image_route_fifteenth))
def serve_imageFifteenth(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_fifteenth:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_fifteenth, image_name)

@app.server.route('{}<image_path>.png'.format(static_image_route_sixteenth))
def serve_imageSixteenth(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_sixteenth:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_sixteenth, image_name) 

# US

@app.server.route('{}<image_path>.png'.format(static_image_route_first_us))
def serve_imageFirst_us(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_first_us:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_first_us, image_name)

@app.server.route('{}<image_path>.png'.format(static_image_route_second_us))
def serve_imageSecond_us(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_second_us:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_second_us, image_name)

@app.server.route('{}<image_path>.png'.format(static_image_route_third_us))
def serve_imageThird_us(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_third_us:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_third_us, image_name)

@app.server.route('{}<image_path>.png'.format(static_image_route_fourth_us))
def serve_imageFourth_us(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_fourth_us:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_fourth_us, image_name)

@app.server.route('{}<image_path>.png'.format(static_image_route_fifth_us))
def serve_imageFifth_us(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_fifth_us:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_fifth_us, image_name)

@app.server.route('{}<image_path>.png'.format(static_image_route_sixth_us))
def serve_imageSixth_us(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_sixth_us:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_sixth_us, image_name)

@app.server.route('{}<image_path>.png'.format(static_image_route_seventh_us))
def serve_imageSeventh_us(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_seventh_us:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_seventh_us, image_name)

@app.server.route('{}<image_path>.png'.format(static_image_route_eigth_us))
def serve_imageEigth_us(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_eigth_us:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_eigth_us, image_name)

@app.server.route('{}<image_path>.png'.format(static_image_route_nineth_us))
def serve_imageNineth_us(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_nineth_us:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_nineth_us, image_name)

@app.server.route('{}<image_path>.png'.format(static_image_route_tenth_us))
def serve_imageTenth_us(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_tenth_us:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_tenth_us, image_name)

@app.server.route('{}<image_path>.png'.format(static_image_route_eleventh_us))
def serve_imageEleventh_us(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_eleventh_us:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_eleventh_us, image_name)

@app.server.route('{}<image_path>.png'.format(static_image_route_twelfth_us))
def serve_imageNTwelvth_us(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_twelfth_us:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_twelfth_us, image_name)

@app.server.route('{}<image_path>.png'.format(static_image_route_thirteenth_us))
def serve_imageThirteenth_us(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_thirteenth_us:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_thirteenth_us, image_name)

@app.server.route('{}<image_path>.png'.format(static_image_route_fourteenth_us))
def serve_imageFourteenth_us(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_fourteenth_us:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_fourteenth_us, image_name)

@app.server.route('{}<image_path>.png'.format(static_image_route_fifteenth_us))
def serve_imageFifteenth_us(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_fifteenth_us:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_fifteenth_us, image_name)

@app.server.route('{}<image_path>.png'.format(static_image_route_sixteenth_us))
def serve_imageSixteenth_us(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_sixteenth_us:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_sixteenth_us, image_name) 



if __name__ == '__main__':
    app.run_server(debug=False)