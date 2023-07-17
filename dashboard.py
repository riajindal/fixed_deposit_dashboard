import dash
import plotly.express as px
from dash import Dash, html, dcc, Input, Output
import socket
from tenure_rates import fig as rate_plot
from comp_interest_rate_plot import fig_1 as tenure_plot
from comp_interest_rate_plot import fig as indiv_plot
from historical_plot import fig as historic_plot

# Dashboard:-

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Fixed Deposit Dashboard", style={'textAlign': 'center'}),
    html.Div(id='none', children=[]),
    dcc.Graph(id='my_bar_chart', figure={}),
    html.H2("Tenure Slabs V/S Interest Rate"),
    dcc.Graph(id='tenure_graph', figure={}),
    html.H2("Individual Tenure Slabs V/S Interest Rate"),
    dcc.Graph(id='indiv_graph', figure={}, style={'height': '800px'}),
    html.H2("SBI Historic Plot"),
    dcc.Graph(id='historic_graph', figure={}, style={'height': '800px'}),
])


@app.callback(
    [Output(component_id='my_bar_chart', component_property='figure'),
     Output(component_id='tenure_graph', component_property='figure'),
     Output(component_id='indiv_graph', component_property='figure'),
     Output(component_id='historic_graph', component_property='figure')],
    [Input(component_id='none', component_property='children')]
)
def update_graph(none):

    figure_1 = rate_plot

    figure_2 = tenure_plot

    figure_3 = indiv_plot

    figure_4 = historic_plot

    return figure_1, figure_2, figure_3, figure_4


def find_available_port():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 0))  # Bind to a random available port
    _, port = sock.getsockname()
    sock.close()
    return port


# Usage
port = find_available_port()
print(f"Available port: {port}")

# Use the port variable in your Dash app configuration
app.run_server(debug=True, port=port)
