from dash import html, dcc
from constants import COLORS, DAY_MARKS
from dash.dependencies import Input, Output
import os

def read_markdown_file():
    """Read the markdown content from explanation.md"""
    with open('explanation.md', 'r', encoding='utf-8') as file:
        return file.read()

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
            
            # Location detection section
            html.Div([
                html.Div([
                    html.H3("📍 Get My Location", 
                            style={
                                'fontFamily': 'Roboto, sans-serif',
                                'fontSize': '18px',
                                'color': COLORS['text'],
                                'marginBottom': '15px',
                                'textAlign': 'center'
                            }),
                    html.Button(
                        "Get Current Date & Location Info",
                        id='location-button',
                        style={
                            'backgroundColor': COLORS['primary'],
                            'color': 'white',
                            'border': 'none',
                            'padding': '12px 24px',
                            'borderRadius': '8px',
                            'fontFamily': 'Roboto, sans-serif',
                            'fontSize': '16px',
                            'cursor': 'pointer',
                            'width': '100%',
                            'marginBottom': '15px',
                            'transition': 'all 0.3s ease'
                        }
                    ),
                    html.Div(
                        id='location-status',
                        style={
                            'fontFamily': 'Roboto, sans-serif',
                            'fontSize': '14px',
                            'color': COLORS['text'],
                            'textAlign': 'center',
                            'fontStyle': 'italic',
                            'whiteSpace': 'pre-line'
                        }
                    ),
                    # Hidden divs to store location data
                    dcc.Store(id='user-latitude', data=None),
                    dcc.Store(id='user-day', data=None),
                ], style={
                    'padding': '20px',
                    'backgroundColor': 'white',
                    'borderRadius': '10px',
                    'boxShadow': '0 2px 4px rgba(0,0,0,0.1)',
                    'marginBottom': '20px'
                }),
            ], style={
                'width': '1000px',
                'margin': '0 auto',
                'padding': '20px'
            }),
            
            # Controls section with uniform width
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
                    'padding': '20px',
                    'backgroundColor': 'white',
                    'borderRadius': '10px',
                    'boxShadow': '0 2px 4px rgba(0,0,0,0.1)'
                }),
            ], style={
                'width': '1000px',
                'margin': '0 auto',
                'padding': '20px'
            }),
            
            # Plots section with uniform width and vertical stacking
            html.Div([
                html.Div([
                    dcc.Graph(id='time-series-plot'),
                ], style={
                    'padding': '10px',
                    'backgroundColor': 'white',
                    'borderRadius': '10px',
                    'boxShadow': '0 2px 4px rgba(0,0,0,0.1)',
                    'marginBottom': '20px'
                }),
                
                html.Div([
                    dcc.Graph(id='polar-plot'),
                ], style={
                    'padding': '10px',
                    'backgroundColor': 'white',
                    'borderRadius': '10px',
                    'boxShadow': '0 2px 4px rgba(0,0,0,0.1)'
                }),
            ], style={
                'width': '1000px',
                'margin': '0 auto',
                'padding': '20px'
            }),
            
            # Explanation section with uniform width
            html.Div([
                html.Div([
                    dcc.Markdown(id='explanation-content', mathjax=True)
                ], style={
                    'padding': '30px',
                    'backgroundColor': 'white',
                    'borderRadius': '10px',
                    'boxShadow': '0 2px 4px rgba(0,0,0,0.1)',
                    'fontFamily': 'Roboto, sans-serif',
                    'fontSize': '16px',
                    'color': COLORS['text'],
                    'lineHeight': '1.6'
                }),
            ], style={
                'width': '1000px',
                'margin': '0 auto',
                'marginTop': '40px',
                'marginBottom': '40px',
                'padding': '20px'
            })
        ], style={
            'backgroundColor': COLORS['background'],
            'minHeight': '100vh',
            'padding': '20px'
        })
    ], style={'fontFamily': 'Roboto, sans-serif'}) 