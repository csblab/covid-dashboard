import dash
import dash_core_components as dcc
import dash_flexbox_grid as dfx
import dash_html_components as html
import flask
import glob
import os
import pathlib

scriptdir = pathlib.Path(os.getcwd())  # this notebook

image_directory_NAmerica = scriptdir / 'plots_gp/North_America'
list_of_images_NAmerica = sorted([str(f).split('/North_America/')[1] for f in list(image_directory_NAmerica.rglob('*'))])
static_image_route_NAmerica = '/staticNA/'

image_directory_SAmerica = scriptdir / 'plots_gp/South_America/'
list_of_images_SAmerica = sorted([ str(f).split('/South_America/')[1] for f in list(image_directory_SAmerica.rglob('*'))])
static_image_route_SAmerica = '/staticSA/'

image_directory_Europe = scriptdir / 'plots_gp/Europe/'
list_of_images_Europe = sorted([ str(f).split('/Europe/')[1] for f in list(image_directory_Europe.rglob('*'))])
static_image_route_Europe = '/staticEU/'

image_directory_Asia = scriptdir / 'plots_gp/Asia/'
list_of_images_Asia = sorted([ str(f).split('/Asia/')[1] for f in list(image_directory_Asia.rglob('*'))])
static_image_route_Asia = '/staticAS/'

image_directory_Africa = scriptdir / 'plots_gp/Africa/'
list_of_images_Africa = sorted([ str(f).split('/Africa/')[1] for f in list(image_directory_Africa.rglob('*'))])
static_image_route_Africa = '/staticAF/'

image_directory_Oceania = scriptdir / 'plots_gp/Oceania/'
list_of_images_Oceania = sorted([ str(f).split('/Oceania/')[1] for f in list(image_directory_Oceania.rglob('*'))])
static_image_route_Oceania = '/staticOC/'

image_directory_Ships = scriptdir / 'plots_gp/Ships/'
list_of_images_Ships = sorted([ str(f).split('/Ships/')[1] for f in list(image_directory_Ships.rglob('*'))])
static_image_route_Ships = '/staticSH/'


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
                     html.H3('North America'),
                     dcc.Dropdown(
                        id='image-dropdownNAmerica',
                        options=[{'label': i, 'value': i} for i in list_of_images_NAmerica],
                        placeholder="Select Country",
                        value=list_of_images_NAmerica[0],
                        style=dict(
                            width='90%',
                            #display='inline-block',
                            verticalAlign = "middle"
                        )
                    ),
                    html.Img(id='imageNAmerica', style={'width': '600px'})
                ]
            ),
            dfx.Col(
                xs=6,
                lg=6, 
                children=[
                    html.H3('South America'),
                    dcc.Dropdown(
                            id='image-dropdownSAmerica',
                            options=[{'label': i, 'value': i} for i in list_of_images_SAmerica],
                            placeholder="Select Country",
                            value=list_of_images_SAmerica[0],
                            style=dict(
                                width='90%',
                                #display='inline-block',
                                verticalAlign = "middle"
                            )
                        ),
                    html.Img(id='imageSAmerica', style={'width': '600px'})
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
                    html.H3('Europe'),
                    dcc.Dropdown(
                        id='image-dropdownEurope',
                        options=[{'label': i, 'value': i} for i in list_of_images_Europe],
                        placeholder="Select Country",
                        value=list_of_images_Europe[0],
                        style=dict(
                            width='90%',
                            #display='inline-block',
                            verticalAlign = "middle"
                        )
                    ),
                    html.Img(id='imageEurope', style={'width': '600px'}),
                ]
            ), 
            dfx.Col(
                xs=6, 
                lg=6, 
                children=[
                    html.H3('Asia'),
                    dcc.Dropdown(
                        id='image-dropdownAsia',
                        options=[{'label': i, 'value': i} for i in list_of_images_Asia],
                        placeholder="Select Country",
                        value=list_of_images_Asia[0],
                        style=dict(
                            width='90%',
                            #display='inline-block',
                            verticalAlign = "middle"
                        )
                    ),
                    html.Img(id='imageAsia', style={'width': '600px'}),
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
                    html.H3('Africa'),
                    dcc.Dropdown(
                        id='image-dropdownAfrica',
                        options=[{'label': i, 'value': i} for i in list_of_images_Africa],
                        placeholder="Select Country",
                        value=list_of_images_Africa[0],
                        style=dict(
                            width='90%',
                            #display='inline-block',
                            verticalAlign = "middle"
                        )
                    ),
                    html.Img(id='imageAfrica', style={'width': '600px'}),
                ]
            ),
             dfx.Col(
                xs=6, 
                lg=6, 
                children=[
                    html.H3('Oceania'),
                    dcc.Dropdown(
                        id='image-dropdownOceania',
                        options=[{'label': i, 'value': i} for i in list_of_images_Oceania],
                        placeholder="Select Country",
                        value=list_of_images_Oceania[0],
                        style=dict(
                            width='90%',
                            #display='inline-block',
                            verticalAlign = "middle"
                        )
                    ),
                    html.Img(id='imageOceania', style={'width': '600px'}),
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
                    html.H3('Ships'),
                    dcc.Dropdown(
                        id='image-dropdownShips',
                        options=[{'label': i, 'value': i} for i in list_of_images_Ships],
                        placeholder="Select Country",
                        value=list_of_images_Ships[0],
                        style=dict(
                            width='90%',
                            #display='inline-block',
                            verticalAlign = "middle"
                        )
                    ),
                    html.Img(id='imageShips', style={'width': '600px'}),
                ]
            ),
        ],
    ),


])

#callbacks
@app.callback(
    dash.dependencies.Output('imageNAmerica', 'src'),
    [dash.dependencies.Input('image-dropdownNAmerica', 'value')]
)
def update_image_srcNAmerica(value):
    return static_image_route_NAmerica + value


@app.callback(
    dash.dependencies.Output('imageSAmerica', 'src'),
    [dash.dependencies.Input('image-dropdownSAmerica', 'value')]
)
def update_image_srcEurope(value):
    return static_image_route_SAmerica + value

@app.callback(
    dash.dependencies.Output('imageEurope', 'src'),
    [dash.dependencies.Input('image-dropdownEurope', 'value')]
)
def update_image_srcEurope(value):
    return static_image_route_Europe + value

@app.callback(
    dash.dependencies.Output('imageAsia', 'src'),
    [dash.dependencies.Input('image-dropdownAsia', 'value')]
)
def update_image_srcAsia(value):
    return static_image_route_Asia + value

@app.callback(
    dash.dependencies.Output('imageAfrica', 'src'),
    [dash.dependencies.Input('image-dropdownAfrica', 'value')]
)
def update_image_srcAfrica(value):
    return static_image_route_Africa + value

@app.callback(
    dash.dependencies.Output('imageOceania', 'src'),
    [dash.dependencies.Input('image-dropdownOceania', 'value')]
)
def update_image_srcOceania(value):
    return static_image_route_Oceania + value

@app.callback(
    dash.dependencies.Output('imageShips', 'src'),
    [dash.dependencies.Input('image-dropdownShips', 'value')]
)
def update_image_srcShips(value):
    return static_image_route_Ships + value    

# Add a static image route that serves images from desktop
# Be *very* careful here - you don't want to serve arbitrary files
# from your computer or server
@app.server.route('{}<image_path>.png'.format(static_image_route_NAmerica))
def serve_imageNAmerica(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_NAmerica:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_NAmerica, image_name)


@app.server.route('{}<image_path>.png'.format(static_image_route_SAmerica))
def serve_imageSAmerica(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_SAmerica:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_SAmerica, image_name)

@app.server.route('{}<image_path>.png'.format(static_image_route_Europe))
def serve_imageEurope(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_Europe:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_Europe, image_name)

@app.server.route('{}<image_path>.png'.format(static_image_route_Asia))
def serve_imageAsia(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_Asia:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_Asia, image_name)

@app.server.route('{}<image_path>.png'.format(static_image_route_Africa))
def serve_imageAfrica(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_Africa:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_Africa, image_name)

@app.server.route('{}<image_path>.png'.format(static_image_route_Oceania))
def serve_imageOceania(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_Oceania:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_Oceania, image_name)    

@app.server.route('{}<image_path>.png'.format(static_image_route_Ships))
def serve_imageShips(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images_Ships:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory_Ships, image_name)    

if __name__ == '__main__':
    app.run_server(debug=False)