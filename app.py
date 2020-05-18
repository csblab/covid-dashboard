import dash
import dash_core_components as dcc
import dash_flexbox_grid as dfx
import dash_html_components as html
import flask
import glob
import os
import pathlib

scriptdir = pathlib.Path(os.getcwd())  # this notebook

image_directory_first = scriptdir / 'plots/cCdD'
list_of_images_first = [str(f).split('/cCdD/')[1] for f in list(image_directory_first.rglob('*.png'))]
static_image_route_first = '/staticfirst/'

image_directory_second = scriptdir / 'plots/cCd='
list_of_images_second = [str(f).split('/cCd=/')[1] for f in list(image_directory_second.rglob('*.png'))]
static_image_route_second = '/staticsecond/'

image_directory_third = scriptdir / 'plots/cC=='
list_of_images_third = [str(f).split('/cC==/')[1] for f in list(image_directory_third.rglob('*.png'))]
static_image_route_third = '/staticthird/'

image_directory_fourth = scriptdir / 'plots/c=dD'
list_of_images_fourth = [str(f).split('/c=dD/')[1] for f in list(image_directory_fourth.rglob('*.png'))]
static_image_route_fourth = '/staticfourth/'

image_directory_fifth = scriptdir / 'plots/c=d='
list_of_images_fifth = [str(f).split('/c=d=/')[1] for f in list(image_directory_fifth.rglob('*.png'))]
static_image_route_fifth = '/staticfifth/'

image_directory_sixth = scriptdir / 'plots/c==D'
list_of_images_sixth = [str(f).split('/c==D/')[1] for f in list(image_directory_sixth.rglob('*.png'))]
static_image_route_sixth = '/staticsixth/'

image_directory_seventh = scriptdir / 'plots/c=d='
list_of_images_seventh = [str(f).split('/c=d=/')[1] for f in list(image_directory_seventh.rglob('*.png'))]
static_image_route_seventh = '/staticseventh/'

image_directory_eigth = scriptdir / 'plots/=CdD'
list_of_images_eigth = [str(f).split('/=CdD/')[1] for f in list(image_directory_eigth.rglob('*.png'))]
static_image_route_eigth = '/staticeigth/'

image_directory_nineth = scriptdir / 'plots/=Cd='
list_of_images_nineth = [str(f).split('/=Cd=/')[1] for f in list(image_directory_nineth.rglob('*.png'))]
static_image_route_nineth = '/staticnineth/'

image_directory_tenth = scriptdir / 'plots/==dD/'
list_of_images_tenth = [ str(f).split('/==dD/')[1] for f in list(image_directory_tenth.rglob('*.png'))]
static_image_route_tenth = '/statictenth/'

image_directory_eleventh = scriptdir / 'plots/==d='
list_of_images_eleventh = [str(f).split('/==d=/')[1] for f in list(image_directory_eleventh.rglob('*.png'))]
static_image_route_eleventh = '/staticeleventh/'

image_directory_twelfth = scriptdir / 'plots/===D'
list_of_images_twelfth = [str(f).split('/===D/')[1] for f in list(image_directory_twelfth.rglob('*.png'))]
static_image_route_twelfth = '/statictwelfth/'

image_directory_thirteenth = scriptdir / 'plots/===='
list_of_images_thirteenth = [str(f).split('/====/')[1] for f in list(image_directory_thirteenth.rglob('*.png'))]
static_image_route_thirteenth = '/staticthirteenth/'




app = dash.Dash(__name__)
server = app.server #for server deployment
app.scripts.config.serve_locally = True

app.layout = dfx.Grid(id='grid', fluid=True, children=[ 
    
    dfx.Row(
        id='row1',
        children=[
            dfx.Col(
                id='col1', 
                xs=6, 
                lg=6, 
                children=[
                     html.H3('cCdD'),
                     dcc.Dropdown(
                        id='image-dropdownFirst',
                        options=[{'label': i, 'value': i} for i in list_of_images_first],
                        placeholder="Select Country",
                        value=list_of_images_first[0],
                        style=dict(
                            width='90%',
                            #display='inline-block',
                            verticalAlign = "middle"
                        )
                    ),
                    html.Img(id='imagefirst', style={'width': '600px'})
                ]
            ),
            dfx.Col(
                xs=6,
                lg=6, 
                children=[
                    html.H3('cCd='),
                    dcc.Dropdown(
                            id='image-dropdownSecond',
                            options=[{'label': i, 'value': i} for i in list_of_images_second],
                            placeholder="Select Country",
                            value=list_of_images_second[0],
                            style=dict(
                                width='90%',
                                #display='inline-block',
                                verticalAlign = "middle"
                            )
                        ),
                    html.Img(id='imagesecond', style={'width': '600px'})
                ]    
            ),
        ]
    ),

    dfx.Row(
        id='row2', 
        children=[ 
            dfx.Col(
                id='col2', 
                xs=6, 
                lg=6, 
                children=[
                    html.H3('cC=='),
                    dcc.Dropdown(
                        id='image-dropdownThird',
                        options=[{'label': i, 'value': i} for i in list_of_images_third],
                        placeholder="Select Country",
                        value=list_of_images_third[0],
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
                xs=6, 
                lg=6, 
                children=[
                    html.H3('c=dD'),
                    dcc.Dropdown(
                        id='image-dropdownFourth',
                        options=[{'label': i, 'value': i} for i in list_of_images_fourth],
                        placeholder="Select Country",
                        value=list_of_images_fourth[0],
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
                id='col3', 
                xs=6, 
                lg=6, 
                children=[
                    html.H3('c=d='),
                    dcc.Dropdown(
                        id='image-dropdownFifth',
                        options=[{'label': i, 'value': i} for i in list_of_images_fifth],
                        placeholder="Select Country",
                        value=list_of_images_fifth[0],
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
                xs=6, 
                lg=6, 
                children=[
                    html.H3('c==D'),
                    dcc.Dropdown(
                        id='image-dropdownSixth',
                        options=[{'label': i, 'value': i} for i in list_of_images_sixth],
                        placeholder="Select Country",
                        value=list_of_images_sixth[0],
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
                id='col4', 
                xs=6, 
                lg=6, 
                children=[
                    html.H3('c==='),
                    dcc.Dropdown(
                        id='image-dropdownSeventh',
                        options=[{'label': i, 'value': i} for i in list_of_images_seventh],
                        placeholder="Select Country",
                        value=list_of_images_seventh[0],
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
                xs=6, 
                lg=6, 
                children=[
                    html.H3('=CdD'),
                    dcc.Dropdown(
                        id='image-dropdownEigth',
                        options=[{'label': i, 'value': i} for i in list_of_images_eigth],
                        placeholder="Select Country",
                        value=list_of_images_eigth[0],
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
                id='col5', 
                xs=6, 
                lg=6, 
                children=[
                    html.H3('=Cd='),
                    dcc.Dropdown(
                        id='image-dropdownNineth',
                        options=[{'label': i, 'value': i} for i in list_of_images_nineth],
                        placeholder="Select Country",
                        value=list_of_images_nineth[0],
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
                xs=6, 
                lg=6, 
                children=[
                    html.H3('==dD'),
                    dcc.Dropdown(
                        id='image-dropdownTenth',
                        options=[{'label': i, 'value': i} for i in list_of_images_tenth],
                        placeholder="Select Country",
                        value=list_of_images_tenth[0],
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
                id='col6', 
                xs=6, 
                lg=6, 
                children=[
                    html.H3('==d='),
                    dcc.Dropdown(
                        id='image-dropdownEleventh',
                        options=[{'label': i, 'value': i} for i in list_of_images_eleventh],
                        placeholder="Select Country",
                        value=list_of_images_eleventh[0],
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
                xs=6, 
                lg=6, 
                children=[
                    html.H3('===D'),
                    dcc.Dropdown(
                        id='image-dropdownTwelfth',
                        options=[{'label': i, 'value': i} for i in list_of_images_twelfth],
                        placeholder="Select Country",
                        value=list_of_images_twelfth[0],
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
                id='col7',
                xs=6,
                lg=6,
                children=[
                    html.H3('===='),
                    dcc.Dropdown(
                        id='image-dropdownThirteenth',
                        options=[{'label': i, 'value': i} for i in list_of_images_thirteenth],
                        placeholder="Select Country",
                        value=list_of_images_thirteenth[0],
                        style=dict(
                            width='90%',
                            #display='inline-block',
                            verticalAlign = "middle"
                        )
                    ),
                    html.Img(id='imagethirteenth', style={'width': '600px'}),
                ]
            ), 
        ]
    )
])

#callbacks
@app.callback(
    dash.dependencies.Output('imagefirst', 'src'),
    [dash.dependencies.Input('image-dropdownFirst', 'value')]
)
def update_image_srcFirst(value):
    return static_image_route_first + value


@app.callback(
    dash.dependencies.Output('imagesecond', 'src'),
    [dash.dependencies.Input('image-dropdownSecond', 'value')]
)
def update_image_srcSecond(value):
    return static_image_route_second + value

@app.callback(
    dash.dependencies.Output('imagethird', 'src'),
    [dash.dependencies.Input('image-dropdownThird', 'value')]
)
def update_image_srcThird(value):
    return static_image_route_third + value    

@app.callback(
    dash.dependencies.Output('imagefourth', 'src'),
    [dash.dependencies.Input('image-dropdownFourth', 'value')]
)
def update_image_srcFourth(value):
    return static_image_route_fourth + value

@app.callback(
    dash.dependencies.Output('imagefifth', 'src'),
    [dash.dependencies.Input('image-dropdownFifth', 'value')]
)
def update_image_srcFifth(value):
    return static_image_route_fifth + value

@app.callback(
    dash.dependencies.Output('imagesixth', 'src'),
    [dash.dependencies.Input('image-dropdownSixth', 'value')]
)
def update_image_srcSixth(value):
    return static_image_route_sixth + value


@app.callback(
    dash.dependencies.Output('imageseventh', 'src'),
    [dash.dependencies.Input('image-dropdownSeventh', 'value')]
)
def update_image_srcSeventh(value):
    return static_image_route_seventh + value
    
@app.callback(                
    dash.dependencies.Output('imageeigth', 'src'),
    [dash.dependencies.Input('image-dropdownEigth', 'value')]
)
def update_image_srcEight(value):
    return static_image_route_eigth + value
    
@app.callback(
    dash.dependencies.Output('imagenineth', 'src'),
    [dash.dependencies.Input('image-dropdownNineth', 'value')]
)
def update_image_srcNineth(value):
    return static_image_route_nineth + value
    
@app.callback(
    dash.dependencies.Output('imagetenth', 'src'),
    [dash.dependencies.Input('image-dropdownTenth', 'value')]
)
def update_image_srcTenth(value):
    return static_image_route_tenth + value
    
@app.callback(
    dash.dependencies.Output('imageeleventh', 'src'),
    [dash.dependencies.Input('image-dropdownEleventh', 'value')]
)
def update_image_srcEleventh(value):
    return static_image_route_eleventh+ value
    
@app.callback(
    dash.dependencies.Output('imagetwelfth', 'src'),
    [dash.dependencies.Input('image-dropdownTwelfth', 'value')]
)
def update_image_srcTwelve(value):
    return static_image_route_twelfth + value

@app.callback(
    dash.dependencies.Output('imagethirteenth', 'src'),
    [dash.dependencies.Input('image-dropdownThirteenth', 'value')]
)
def update_image_srcThirteenth(value):
    return static_image_route_thirteenth + value    
# Add a static image route that serves images from desktop
# Be *very* careful here - you don't want to serve arbitrary files
# from your computer or server

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

if __name__ == '__main__':
    app.run_server(debug=False)