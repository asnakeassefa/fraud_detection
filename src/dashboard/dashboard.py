from dash import Dash, dcc, html, Input, Output
import requests
import pandas as pd
import plotly.express as px

# Initialize Dash app
app = Dash(__name__, suppress_callback_exceptions=True)
app.title = "Fraud Insights Dashboard"

# Fetch data from Flask backend
def fetch_data(endpoint):
    response = requests.get(f'http://127.0.0.1:5000/api/{endpoint}')
    return pd.DataFrame(response.json())

# Layout for the dashboard
app.layout = html.Div([
    html.H1("Fraud Detection Dashboard", style={'textAlign': 'center'}),

    # Summary Boxes
    html.Div(id='summary', style={'display': 'flex', 'justify-content': 'space-around'}),

    # Line Chart for Fraud Trends
    html.Div([
        html.H3("Fraud Cases Over Time"),
        dcc.Graph(id='fraud-trends'),
    ]),

    # Geography Analysis
    html.Div([
        html.H3("Fraud Cases by Geography"),
        dcc.Graph(id='fraud-geo'),
    ]),

    # Device and Browser Analysis
    html.Div([
        html.H3("Fraud Cases by Device and Browser"),
        dcc.Graph(id='device-browser'),
    ]),
])

# Callbacks to populate the dashboard
@app.callback(
    Output('summary', 'children'),
    Input('summary', 'id')
)
def update_summary(_):
    data = fetch_data('summary')
    return [
        html.Div([
            html.H4("Total Transactions"),
            html.P(f"{data['total_transactions'][0]}")
        ]),
        html.Div([
            html.H4("Fraud Cases"),
            html.P(f"{data['fraud_cases'][0]}")
        ]),
        html.Div([
            html.H4("Fraud Percentage"),
            html.P(f"{data['fraud_percentage'][0]}%")
        ]),
    ]

@app.callback(
    Output('fraud-trends', 'figure'),
    Input('fraud-trends', 'id')
)
def update_fraud_trends(_):
    data = fetch_data('fraud_trends')
    fig = px.line(data, x='signup_time', y='class', title='Fraud Cases Over Time')
    return fig

@app.callback(
    Output('fraud-geo', 'figure'),
    Input('fraud-geo', 'id')
)
def update_geo_analysis(_):
    data = fetch_data('fraud_geography')
    fig = px.bar(data, x='source_Direct', y='class', title='Fraud Cases by Geography')
    return fig

@app.callback(
    Output('device-browser', 'figure'),
    Input('device-browser', 'id')
)
def update_device_browser(_):
    data = fetch_data('device_browser')
    fig = px.bar(data, x='browser_Safari', y='class', color='browser_Opera', title='Fraud Cases by Device and Browser')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
