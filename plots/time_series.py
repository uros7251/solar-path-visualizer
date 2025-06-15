import plotly.graph_objects as go
from constants import COLORS

def create_time_series_plot(hour_angles, altitude, azimuth, latitude, day):
    """Create the time series plot showing altitude and azimuth over time."""
    fig = go.Figure()
    
    # Add altitude trace
    fig.add_trace(go.Scatter(
        x=hour_angles,
        y=altitude,
        mode='lines',
        name='Altitude',
        line=dict(color=COLORS['primary'], width=3)
    ))
    
    # Add azimuth trace
    fig.add_trace(go.Scatter(
        x=hour_angles,
        y=azimuth,
        mode='lines',
        name='Azimuth',
        line=dict(color=COLORS['secondary'], width=3)
    ))
    
    # Update layout
    fig.update_layout(
        title=dict(
            text=f'Time Series (Latitude: {latitude}°, Day: {day})',
            font=dict(
                family='Roboto, sans-serif',
                size=20,
                color=COLORS['text']
            )
        ),
        xaxis_title='Hour Angle (degrees)',
        yaxis_title='Degrees',
        xaxis=dict(
            range=[-180, 180],
            gridcolor=COLORS['grid'],
            zerolinecolor=COLORS['grid']
        ),
        yaxis=dict(
            range=[-90, 360],
            gridcolor=COLORS['grid'],
            zerolinecolor=COLORS['grid']
        ),
        showlegend=True,
        hovermode='closest',
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(
            family='Roboto, sans-serif',
            size=12,
            color=COLORS['text']
        ),
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01,
            bgcolor='rgba(255, 255, 255, 0.8)'
        )
    )
    
    # Add reference lines
    fig.add_hline(y=0, line_dash="dash", line_color=COLORS['grid'], opacity=0.5)
    fig.add_vline(x=0, line_dash="dash", line_color=COLORS['grid'], opacity=0.5)
    
    return fig 