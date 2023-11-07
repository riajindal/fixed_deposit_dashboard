import math
import os
import sys
import dash
import pandas as pd
import plotly.express as px
from dash import html, dcc, callback, Input, Output
from plotly.subplots import make_subplots
from utility import master
from definition import ROOT_PATH

PROJECT_ROOT = os.path.dirname(os.path.abspath(ROOT_PATH))

# Add the project root to the Python path
sys.path.insert(0, PROJECT_ROOT)

# Register page as a page on the dashboard
dash.register_page(__name__, path='/', name='Home')

# Define options to be displayed in dropdown
options = [{'label': bank.name, 'value': bank.name} for bank in master]

# Get repo rate from .txt file
with open('repo_rate.txt', 'r') as file:
    repo_rate = file.read()

# Create HTML page layout
layout = html.Div([
    html.H2("Tenure V/S Interest Rate"),
    dcc.Graph(id='tenure_graph', figure={}, className='mb-4'),
    html.H2("Individual Tenure Slabs V/S Interest Rate"),
    dcc.Dropdown(
        id='my_dropdown',
        options=options,
        optionHeight=35,
        value=['HDFC'],
        multi=True,
        clearable=True,
        style={'width': '50%'}
    ),
    dcc.Graph(id='indiv_graph', figure={}, style={'height': '800px'}),
])


# Callback function to add functionality to page
@callback(
    [Output(component_id='tenure_graph', component_property='figure'),
     Output(component_id='indiv_graph', component_property='figure')],
    [Input(component_id='my_dropdown', component_property='value')]
)
def update_graph(my_dropdown):
    x_axis_order = master[1].df['Tenure']
    bucket_master = pd.read_csv(r'bucket_master.csv')
    banks = [column for column in bucket_master.columns if column != "Tenure"]
    figure_1 = px.line(bucket_master, x='Tenure', y=banks, markers=True)
    figure_1.add_hline(y=float(repo_rate), annotation_text=f'RBI Repo Rate {repo_rate}', annotation_position='top left')
    figure_1.update_xaxes(categoryorder='array', categoryarray=x_axis_order)

    figure_2 = px.line(bucket_master, x='Tenure', y=my_dropdown, markers=True)
    figure_2.add_hline(y=float(repo_rate), annotation_text=f'RBI Repo Rate {repo_rate}', annotation_position='top left')

    return figure_1, figure_2
