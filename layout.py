from dash import html, dcc
from constants import COLORS, DAY_MARKS

def create_layout():
    """Create the main layout of the application."""
    return html.Div([
        html.Div([
            html.H1("Sun Movement Visualization", 
                    style={
                        'textAlign': 'center',
                        'color': COLORS['text'],
                        'fontFamily': 'Roboto, sans-serif',
                        'fontWeight': '300',
                        'marginBottom': '30px',
                        'marginTop': '20px'
                    }),
            
            html.Div([
                html.Div([
                    html.Label("Latitude (degrees)", 
                              style={
                                  'fontFamily': 'Roboto, sans-serif',
                                  'fontSize': '16px',
                                  'color': COLORS['text'],
                                  'marginBottom': '10px',
                                  'display': 'block'
                              }),
                    dcc.Slider(
                        id='latitude-slider',
                        min=-90,
                        max=90,
                        value=45,
                        marks={i: f'{i}°' for i in range(-90, 91, 30)},
                        step=1,
                        className='custom-slider'
                    ),
                ], style={
                    'marginBottom': '30px',
                    'padding': '20px',
                    'backgroundColor': 'white',
                    'borderRadius': '10px',
                    'boxShadow': '0 2px 4px rgba(0,0,0,0.1)'
                }),
                
                html.Div([
                    html.Label("Time of Year", 
                              style={
                                  'fontFamily': 'Roboto, sans-serif',
                                  'fontSize': '16px',
                                  'color': COLORS['text'],
                                  'marginBottom': '10px',
                                  'display': 'block'
                              }),
                    dcc.Slider(
                        id='day-slider',
                        min=1,
                        max=366,  # Using 366 to account for leap year
                        value=182,  # July 1st
                        marks=DAY_MARKS,
                        step=1,
                        className='custom-slider'
                    ),
                    html.Div(id='declination-info', 
                            style={
                                'fontFamily': 'Roboto, sans-serif',
                                'fontSize': '14px',
                                'color': COLORS['text'],
                                'marginTop': '10px',
                                'textAlign': 'center',
                                'fontStyle': 'italic'
                            }),
                ], style={
                    'flex': '1',
                    'padding': '20px',
                    'backgroundColor': 'white',
                    'borderRadius': '10px',
                    'boxShadow': '0 2px 4px rgba(0,0,0,0.1)'
                }),
            ], style={'width': '80%', 'margin': '0 auto', 'padding': '20px'}),
            
            html.Div([
                html.Div([
                    dcc.Graph(id='time-series-plot'),
                ], style={
                    'flex': '1',
                    'minWidth': '500px',
                    'padding': '10px',
                    'backgroundColor': 'white',
                    'borderRadius': '10px',
                    'boxShadow': '0 2px 4px rgba(0,0,0,0.1)'
                }),
                
                html.Div([
                    dcc.Graph(id='polar-plot'),
                ], style={
                    'flex': '1',
                    'minWidth': '500px',
                    'padding': '10px',
                    'backgroundColor': 'white',
                    'borderRadius': '10px',
                    'boxShadow': '0 2px 4px rgba(0,0,0,0.1)'
                }),
            ], style={
                'display': 'flex',
                'flexWrap': 'wrap',
                'gap': '20px',
                'justifyContent': 'center',
                'width': '95%',
                'margin': '0 auto'
            }),
        ], style={
            'backgroundColor': COLORS['background'],
            'minHeight': '100vh',
            'padding': '20px'
        })
    ], style={'fontFamily': 'Roboto, sans-serif'}) 