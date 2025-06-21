import plotly.graph_objects as go
import numpy as np
from constants import COLORS

# Polar plot radius - can be easily changed here
POLAR_RADIUS = 1

# Customizable colormap - change this to experiment with different gradients
# Options: 'plasma', 'viridis', 'inferno', 'magma', 'cividis', 'coolwarm', 'RdYlBu', 'Spectral', etc.
SUN_PATH_COLORMAP = 'Spectral_r'

def add_polar_grid(fig):
    """Add grid lines and circles to the polar plot."""
    # Add circles for altitude reference - proportional to radius
    for r_ratio in [0.25, 0.5, 0.75, 1.0]:
        r = POLAR_RADIUS * r_ratio
        theta = np.linspace(0, 2*np.pi, 100)
        fig.add_trace(go.Scatter(
            x=r * np.cos(theta),
            y=r * np.sin(theta),
            mode='lines',
            line=dict(color=COLORS['grid'], width=1, dash='dot'),
            showlegend=False,
            hoverinfo='skip'
        ))
    
    # Add radial grid lines at 30-degree intervals, extended to match largest circle
    for angle in np.arange(0, 360, 30):
        phi = np.radians(angle)
        fig.add_trace(go.Scatter(
            x=[0, POLAR_RADIUS * np.sin(phi)],
            y=[0, POLAR_RADIUS * np.cos(phi)],
            mode='lines',
            line=dict(color=COLORS['grid'], width=1, dash='dot'),
            showlegend=False,
            hoverinfo='skip'
        ))

def add_sun_path(fig, altitude, azimuth):
    """Add the sun path with gradient color based on altitude, and mark sunrise/sunset points."""
    import matplotlib.cm as cm

    # Filter for positive altitude (above horizon)
    mask = altitude > 0
    altitude_visible = altitude[mask]
    azimuth_visible = azimuth[mask]

    if len(altitude_visible) > 1:
        # Calculate polar coordinates: r = R * cos(altitude) where R is the radius of polar plot
        r = POLAR_RADIUS * np.cos(np.radians(altitude_visible))
        phi = np.radians(azimuth_visible)

        x = r * np.sin(phi)
        y = r * np.cos(phi)

        # Normalize altitudes to 0-1 using theoretical range (0° to 90°)
        norm_alt = np.clip(altitude_visible / 90.0, 0, 1)
        cmap = cm.get_cmap(SUN_PATH_COLORMAP)
        rgba = cmap(norm_alt)
        colors = [f"rgba({int(r*255)}, {int(g*255)}, {int(b*255)}, 1)" for r, g, b, a in rgba]

        # Create one scatter trace per segment
        for i in range(len(x) - 1):
            # Calculate average altitude for this segment
            avg_altitude = (altitude_visible[i] + altitude_visible[i+1]) / 2
            avg_azimuth = (azimuth_visible[i] + azimuth_visible[i+1]) / 2
            
            fig.add_trace(go.Scatter(
                x=[x[i], x[i+1]],
                y=[y[i], y[i+1]],
                mode='lines',
                line=dict(color=colors[i], width=4),
                showlegend=False,
                hoverinfo='text',
                hovertext=f'Altitude: {avg_altitude:.0f}°<br>Azimuth: {avg_azimuth:.0f}°'
            ))

        # Add dummy scatter for colorbar
        fig.add_trace(go.Scatter(
            x=[None],
            y=[None],
            mode='markers',
            marker=dict(
                colorscale=SUN_PATH_COLORMAP,
                cmin=0,  # Theoretical minimum altitude
                cmax=90,  # Theoretical maximum altitude
                color=[altitude_visible[0]],  # dummy value
                size=0.0001,
                colorbar=dict(
                    title='Altitude (°)',
                    thickness=20,
                    len=0.8,
                    y=0.5
                )
            ),
            showlegend=False
        ))

    # Find sunrise and sunset points (where altitude crosses zero)
    zero_crossings = np.where(np.diff(np.signbit(altitude)))[0]
    sunrise_sunset_azimuth = azimuth[zero_crossings]
    sunrise_sunset_phi = np.radians(sunrise_sunset_azimuth)

    # Add sunrise/sunset points at the circumference (r = POLAR_RADIUS) with 0 altitude color
    if len(sunrise_sunset_azimuth) > 0:
        # Get color for 0 altitude from colormap
        cmap = cm.get_cmap(SUN_PATH_COLORMAP)
        rgba_0 = cmap(0.0)  # 0.0 corresponds to the lowest value in the colormap
        horizon_color = f"rgba({int(rgba_0[0]*255)}, {int(rgba_0[1]*255)}, {int(rgba_0[2]*255)}, 1)"
        
        fig.add_trace(go.Scatter(
            x=POLAR_RADIUS * np.sin(sunrise_sunset_phi),
            y=POLAR_RADIUS * np.cos(sunrise_sunset_phi),
            mode='markers',
            name='Horizon Crossing',
            marker=dict(color=horizon_color, size=12),
            showlegend=False
        ))

        # Add azimuth labels - positioned further out
        label_radius = POLAR_RADIUS * 1.2  # 20% beyond the circumference
        for phi, az in zip(sunrise_sunset_phi, sunrise_sunset_azimuth):
            x = label_radius * np.sin(phi)
            y = label_radius * np.cos(phi)
            fig.add_annotation(
                x=x, y=y,
                text=f'{az:.1f}°',
                showarrow=False,
                font=dict(
                    size=14,
                    color=horizon_color,  # Use same color as horizon points
                    family='Roboto, sans-serif'
                ),
                xanchor='center',
                yanchor='middle'
            )


def add_compass_points(fig):
    """Add compass points (N, E, S, W) to the polar plot."""
    # Position compass points outside the circle
    compass_radius = POLAR_RADIUS * 1.1  # 10% beyond the circumference
    compass_points = {
        'N': (0, compass_radius),
        'E': (compass_radius, 0),
        'S': (0, -compass_radius),
        'W': (-compass_radius, 0)
    }
    
    for point, (x, y) in compass_points.items():
        fig.add_annotation(
            x=x, y=y,
            text=f'<b>{point}</b>',  # Use HTML bold tags
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
    
    # Calculate plot range to accommodate compass points and labels
    plot_range = POLAR_RADIUS * 1.3  # 30% beyond radius to include compass points and labels
    
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
            range=[-plot_range, plot_range],
            showgrid=False,  # Disable rectangular grid to avoid conflicts
            zeroline=False,  # Disable zero line to avoid conflicts
            showticklabels=False,
            scaleanchor='y'
        ),
        yaxis=dict(
            range=[-plot_range, plot_range],
            showgrid=False,  # Disable rectangular grid to avoid conflicts
            zeroline=False,  # Disable zero line to avoid conflicts
            showticklabels=False,
            scaleanchor='x'
        ),
        showlegend=True,
        hovermode='closest',
        # hoverdistance=20,  # Reduce hover distance for more stable behavior
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(
            family='Roboto, sans-serif',
            size=12,
            color=COLORS['text']
        )
    )
    
    return fig 