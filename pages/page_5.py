import os
import sys
import dash
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
from datetime import date, datetime
from utility import master
from definition import ROOT_PATH

PROJECT_ROOT = os.path.dirname(os.path.abspath(ROOT_PATH))
# Add the project root to the Python path
sys.path.insert(0, PROJECT_ROOT)

# Register page as a page on the dashboard
dash.register_page(__name__, path='/page-5', name='Historical Analysis')

# Define options to be displayed in dropdown
options = [{'label': bank.name, 'value': bank.name} for bank in master]

# Create HTML page layout
layout = html.Div(id='div', children=[
    html.H2("Historical Trend for Individual Banks", className='mb-3'),
    dbc.Row([
        dbc.Col([
            dbc.Label("Enter start date and end date", className='d-block'),
            dcc.DatePickerRange(
                id='selected_date',
                min_date_allowed=date(2023, 7, 21),
                max_date_allowed=date.today(),
                initial_visible_month=date(2023, 7, 21),
                start_date=date(2023, 7, 21),
                end_date=date.today(),
                className='d-block'
            ),
        ]),
        dbc.Col([
            dbc.Label("Select Bank"),
            dcc.Dropdown(
                id='bank',
                options=options,
                optionHeight=35,
                value='AXIS',
                clearable=True,
                style={'width': '50%'}
            ),
        ]),
    ], className='w-75 mb-2'),
    dcc.Graph(id='historical_graph_indiv', figure={}, style={'height': '800px'}),
])


# Callback function to add functionality to page
@callback(
    [Output(component_id='historical_graph_indiv', component_property='figure')],
    [Input(component_id='div', component_property='children'),
     Input(component_id='selected_date', component_property='start_date'),
     Input(component_id='selected_date', component_property='end_date'),
     Input(component_id='bank', component_property='value')]
)
def update_graph(none, start_date, end_date, bank):
    # Retrieve files from directory
    files = os.listdir(r'bank_historical_data')
    historical_files = [file_name for file_name in files if file_name.startswith("historical")]
    df_data = []

    # Get date from .csv file name
    def get_date(filename):
        d = filename.split("_", 1)[1]
        d = d.replace("_", "-").replace('.csv', '')
        return d

    # Convert date from string to datetime format
    # for further manipulation and usage
    def format_date(value):
        res = datetime.strptime(value, "%Y-%m-%d")
        res = datetime.strftime(res, "%d-%m-%Y")
        res = pd.to_datetime(res, dayfirst=True)
        return res

    # Get the closest .csv file matching the input date
    def get_closest_date(value, df):
        return min(df['Date'], key=lambda x: abs(x - value))

    # Create list of json objects for filenames and their respective dates
    for file in historical_files:
        new_row = {
            'Date': get_date(file),
            'Filename': file,
        }
        df_data.append(new_row)

    # Create the data frame using list created above and sort according to dates
    df = pd.DataFrame(df_data)
    df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')
    df = df.sort_values(by='Date', ignore_index=True)

    # Format the inputted date by user into appropriate
    # Datetime format for computation using custom function
    # as defined above
    start_date = format_date(start_date)
    end_date = format_date(end_date)

    # Get the nearest date according to files stored
    # in directory for accessing values and creating graph
    new_start_date = get_closest_date(start_date, df)
    new_end_date = get_closest_date(end_date, df)

    # Retrieve the required .csv files
    result_1 = df.loc[df['Date'] == new_start_date, 'Filename'].iloc[0]
    df_1 = pd.read_csv(f'bank_historical_data/{result_1}')
    result_2 = df.loc[df['Date'] == new_end_date, 'Filename'].iloc[0]
    df_2 = pd.read_csv(f'bank_historical_data/{result_2}')

    # Create consolidated data frame to plot comparison
    compare_df = pd.DataFrame(index=list(range(3651)))
    compare_df['Old'] = df_1[bank]
    compare_df['New'] = df_2[bank]

    # Create graph for comparison
    fig = px.line(compare_df, x=compare_df.index, y=['Old', 'New'])

    # fig = make_subplots(rows=1, cols=2, subplot_titles=['Start', 'End'])
    # fig.add_trace(px.line(df_1, x=df_1.index, y=bank).data[0], row=1, col=1)
    # fig.add_trace(px.line(df_2, x=df_2.index, y=bank).data[0], row=1, col=2)

    return [fig]
