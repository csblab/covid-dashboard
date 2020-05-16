import dash
import dash_core_components as dcc
import dash_flexbox_grid as dfx
import dash_html_components as html
import flask
import glob
import os
import pathlib

scriptdir = pathlib.Path(os.getcwd())  # this notebook

image_directory_NAmerica = scriptdir / 'plots/North_America/'

list_of_images_NAmerica = [os.path.basename(x) for x in glob.glob('{}*.png'.format(image_directory_NAmerica))]
static_image_route_NAmerica = '/staticNA/'

image_directory_SAmerica = scriptdir / 'plots/South_America/'
list_of_images_SAmerica = [os.path.basename(x) for x in glob.glob('{}*.png'.format(image_directory_SAmerica))]
static_image_route_SAmerica = '/staticSA/'

image_directory_Europe = scriptdir / 'plots/Europe/'
list_of_images_Europe = [os.path.basename(x) for x in glob.glob('{}*.png'.format(image_directory_Europe))]
static_image_route_Europe = '/staticEU/'

image_directory_Asia = scriptdir / 'plots/Asia/'
list_of_images_Asia = [os.path.basename(x) for x in glob.glob('{}*.png'.format(image_directory_Asia))]
static_image_route_Asia = '/staticAS/'

image_directory_Africa = scriptdir / 'plots/Africa/'
list_of_images_Africa = [os.path.basename(x) for x in glob.glob('{}*.png'.format(image_directory_Africa))]
static_image_route_Africa = '/staticAF/'

app = dash.Dash(__name__)
server = app.server #for server deployment
app.scripts.config.serve_locally = True

app.layout = dfx.Grid(id='grid', fluid=True, children=[ 
    # dfx.Row(children=[ 
    #     dfx.Col(xs=12, lg=3, children=[ 
    #         html.Div('Hello,'), html.Div('World!')
    #     ])
    # ]), 
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
            
        ]
    )

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

if __name__ == '__main__':
    app.run_server(debug=False)