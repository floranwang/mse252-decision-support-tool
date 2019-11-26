import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output
from dash.dependencies import Input
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1('Decision Support Tool', style={'fontSize': '30px'}),

    html.P([
        html.Label('Definition of Storm (number of days of rain)'),
        dcc.Slider(
            id="storm-def",
            min=1,
            max=7,
            marks={i: '{}'.format(i) for i in range(1,8)},
            value=3,
        )], style = {'width' : '50%',
                    'fontSize' : '20px',
                    'padding-top': '10px',
                    'padding-left' : '100px',
                    'padding-bottom': '50px',
                    'display': 'inline-block'}
        ),


    html.P([
        html.Label('Probability that it will storm'),
        dcc.Slider(
            id="storm-prob",
            min=0,
            max=100,
            value=50,
            marks={
            0: {'label': '0%'},
            100: {'label': '100%'}
            }
        )], style = {'width' : '50%',
                    'fontSize' : '20px',
                    'padding-left' : '100px',
                    'padding-bottom': '20px',
                    'display': 'inline-block'}
        ),

    html.Div(id='storm-prob-container', style= {'width' : '50%',
                    'fontSize' : '15px',
                    'padding-left' : '100px',
                    'padding-bottom': '30px',
                    'display': 'inline-block'}
    ),

    html.P([
        html.Label('Risk Aversion', style = {'fontSize' : '20px'}),
        dcc.Input(
            id='risk-aversion',
            type='number',
            value=3
        ),
    ], style = {'width' : '50%',
                'padding-left' : '100px',
                'padding-bottom': '20px',
                'display': 'inline-block'}),

    html.P([
        html.Label('Value of information'),
        html.P(id='value-info')
    ],
    style = {'width' : '50%',
            'fontSize' : '20px',
            'padding-left' : '100px',
            'padding-bottom': '20px',
            'display': 'inline-block'}),

    html.P([
        html.Label('Value of control'),
        html.P(id='value-control')
    ],
    style = {'width' : '50%',
            'fontSize' : '20px',
            'padding-left' : '100px',
            'padding-bottom': '20px',
            'display': 'inline-block'})


], style ={'marginLeft': 10, 'marginRight': 10, 'marginTop': 10, 'marginBottom': 10,})

@app.callback(Output('storm-prob-container', 'children'), [Input('storm-prob', 'value')])
def update_stormProb(value):
    return 'You believe that there is a {}% probability of a storm occuring'.format(value)

@app.callback(Output('value-info', 'children'), [Input('storm-prob', 'value')])
def calc_valueInfo(storm_prob):
    # calculate value of detector
    value = 0
    return 'The value obtained from the weather data is {}. If the data cost more \
    than that, you should NOT buy the data'.format(value)

@app.callback(Output('value-control', 'children'), [Input('storm-prob', 'value')])
def calc_valueInfo(storm_prob):
    # calculate value of spores
    value = 0
    return 'The value obtained from the spores is {}. If the spores cost more \
    than that, you should NOT buy the data'.format(value)

if __name__ == '__main__':
    app.run_server(debug=True)
