from dash import html, dcc
from constants import DAY_MARKS
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
            html.H1("Sun Movement Visualization", className='app-title'),
            
            # Location detection section
            html.Div([
                html.Div([
                    html.H3("📍 Get My Location", className='section-title'),
                    html.Button(
                        "Get Current Date & Location Info",
                        id='location-button',
                        className='location-button'
                    ),
                    html.Div(
                        id='location-status',
                        className='location-status'
                    ),
                    # Hidden divs to store location data
                    dcc.Store(id='user-latitude', data=None),
                    dcc.Store(id='user-day', data=None),
                ], className='location-section'),
            ], className='content-section'),
            
            # Controls section
            html.Div([
                html.Div([
                    html.Label("Latitude (degrees)", className='control-label'),
                    dcc.Slider(
                        id='latitude-slider',
                        min=-90,
                        max=90,
                        value=45,
                        marks={i: f'{i}°' for i in range(-90, 91, 30)},
                        step=1,
                        className='custom-slider'
                    ),
                ], className='control-section'),
                
                html.Div([
                    html.Label("Time of Year", className='control-label'),
                    dcc.Slider(
                        id='day-slider',
                        min=1,
                        max=366,  # Using 366 to account for leap year
                        value=182,  # July 1st
                        marks=DAY_MARKS,
                        step=1,
                        className='custom-slider'
                    ),
                    html.Div(id='declination-info', className='declination-info'),
                ], className='control-section'),
            ], className='content-section'),
            
            # Plots section
            html.Div([
                html.Div([
                    dcc.Graph(id='time-series-plot'),
                ], className='plot-container'),
                
                html.Div([
                    dcc.Graph(id='polar-plot'),
                ], className='plot-container'),
            ], className='content-section'),
            
            # Explanation section
            html.Div([
                html.Div([
                    dcc.Markdown(id='explanation-content', mathjax=True)
                ], className='explanation-container'),
            ], className='content-section explanation-section')
        ], className='main-container')
    ], style={'fontFamily': 'Roboto, sans-serif'}) 