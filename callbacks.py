from dash.dependencies import Input, Output, State
from dash import callback_context
from sun_calculations import calculate_sun_position
from plots.time_series import create_time_series_plot
from plots.polar import create_polar_plot
from layout import read_markdown_file
import datetime

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

    # Clientside callback for geolocation
    app.clientside_callback(
        """
        function(n_clicks) {
            return getCurrentLocationAndDate(n_clicks);
        }
        """,
        [Output('user-latitude', 'data'),
         Output('user-day', 'data'),
         Output('location-status', 'children')],
        [Input('location-button', 'n_clicks')]
    )

    # Callback to update sliders when location is detected
    @app.callback(
        [Output('latitude-slider', 'value'),
         Output('day-slider', 'value')],
        [Input('user-latitude', 'data'),
         Input('user-day', 'data')],
        [State('latitude-slider', 'value'),
         State('day-slider', 'value')]
    )
    def update_sliders_from_location(user_lat, user_day, current_lat, current_day):
        ctx = callback_context
        if not ctx.triggered:
            return current_lat, current_day
        
        # Check if we have both latitude and day data from the location detection
        if user_lat is not None and user_day is not None:
            return user_lat, user_day
        elif user_lat is not None:
            return user_lat, current_day
        elif user_day is not None:
            return current_lat, user_day
        else:
            return current_lat, current_day 