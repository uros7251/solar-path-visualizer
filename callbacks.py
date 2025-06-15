from dash.dependencies import Input, Output
from sun_calculations import calculate_sun_position
from plots.time_series import create_time_series_plot
from plots.polar import create_polar_plot
from layout import read_markdown_file

def register_callbacks(app):
    @app.callback(
        [Output('time-series-plot', 'figure'),
         Output('polar-plot', 'figure'),
         Output('declination-info', 'children')],
        [Input('latitude-slider', 'value'),
         Input('day-slider', 'value')]
    )
    def update_figure(latitude, day):
        # Calculate sun positions
        hour_angles, altitude, azimuth, declination = calculate_sun_position(latitude, day)
        
        # Create plots
        time_series = create_time_series_plot(hour_angles, altitude, azimuth, latitude, day)
        polar = create_polar_plot(altitude, azimuth)
        
        # Create declination info text
        declination_info = f"Solar declination: {declination:.1f}°"
        
        return time_series, polar, declination_info

    @app.callback(
        Output('explanation-content', 'children'),
        Input('explanation-content', 'id')
    )
    def update_explanation(_):
        return read_markdown_file() 