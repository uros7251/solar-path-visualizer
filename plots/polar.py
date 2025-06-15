import plotly.graph_objects as go
import numpy as np
from constants import COLORS

def add_polar_grid(fig):
    """Add grid lines and circles to the polar plot."""
    # Add circles for altitude reference
    for r in [0.25, 0.5, 0.75, 1.0]:
        theta = np.linspace(0, 2*np.pi, 100)
        fig.add_trace(go.Scatter(
            x=r * np.cos(theta),
            y=r * np.sin(theta),
            mode='lines',
            line=dict(color=COLORS['grid'], width=1, dash='dot'),
            showlegend=False
        ))
    
    # Add radial grid lines at 30-degree intervals
    for angle in np.arange(0, 360, 30):
        phi = np.radians(angle)
        fig.add_trace(go.Scatter(
            x=[0, np.sin(phi)],
            y=[0, np.cos(phi)],
            mode='lines',
            line=dict(color=COLORS['grid'], width=1, dash='dot'),
            showlegend=False,
            hoverinfo='skip'
        ))

def add_sun_path(fig, altitude, azimuth):
    """Add the sun path and sunrise/sunset points to the polar plot."""
    # Calculate polar coordinates for ground projection
    r = np.cos(np.radians(altitude))
    phi = np.radians(azimuth)
    
    # Filter for positive altitude
    mask = altitude > 0
    r = r[mask]
    phi = phi[mask]
    
    # Find sunrise and sunset points
    zero_crossings = np.where(np.diff(np.signbit(altitude)))[0]
    sunrise_sunset_azimuth = azimuth[zero_crossings]
    sunrise_sunset_phi = np.radians(sunrise_sunset_azimuth)
    
    # Add polar projection trace
    fig.add_trace(go.Scatter(
        x=r * np.sin(phi),
        y=r * np.cos(phi),
        mode='lines',
        name='Sun Path',
        line=dict(color=COLORS['sun_path'], width=3)
    ))
    
    # Add sunrise/sunset points
    if len(sunrise_sunset_azimuth) > 0:
        fig.add_trace(go.Scatter(
            x=np.sin(sunrise_sunset_phi),
            y=np.cos(sunrise_sunset_phi),
            mode='markers',
            name='Horizon Crossing',
            marker=dict(color=COLORS['sunrise_sunset'], size=12),
            showlegend=False
        ))
        
        # Add azimuth labels
        for phi, az in zip(sunrise_sunset_phi, sunrise_sunset_azimuth):
            x = 1.2 * np.sin(phi)
            y = 1.2 * np.cos(phi)
            fig.add_annotation(
                x=x, y=y,
                text=f'{az:.1f}°',
                showarrow=False,
                font=dict(
                    size=14,
                    color=COLORS['sunrise_sunset'],
                    family='Roboto, sans-serif'
                ),
                xanchor='center',
                yanchor='middle'
            )

def add_compass_points(fig):
    """Add compass points (N, E, S, W) to the polar plot."""
    compass_points = {
        'N': (0, 1.1),
        'E': (1.1, 0),
        'S': (0, -1.1),
        'W': (-1.1, 0)
    }
    
    for point, (x, y) in compass_points.items():
        fig.add_annotation(
            x=x, y=y,
            text=point,
            showarrow=False,
            font=dict(
                size=20,
                color=COLORS['compass'],
                family='Roboto, sans-serif'
            ),
            xanchor='center',
            yanchor='middle'
        )

def create_polar_plot(altitude, azimuth):
    """Create the polar plot showing the sun path projection."""
    fig = go.Figure()
    
    # Add grid and reference elements
    add_polar_grid(fig)
    add_sun_path(fig, altitude, azimuth)
    add_compass_points(fig)
    
    # Update layout
    fig.update_layout(
        title=dict(
            text='Polar Projection',
            font=dict(
                family='Roboto, sans-serif',
                size=20,
                color=COLORS['text']
            )
        ),
        xaxis=dict(
            range=[-1.2, 1.2],
            showgrid=True,
            zeroline=True,
            showticklabels=False,
            scaleanchor='y',
            gridcolor=COLORS['grid'],
            zerolinecolor=COLORS['grid']
        ),
        yaxis=dict(
            range=[-1.2, 1.2],
            showgrid=True,
            zeroline=True,
            showticklabels=False,
            scaleanchor='x',
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
        )
    )
    
    return fig 