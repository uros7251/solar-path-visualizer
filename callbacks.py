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
            if (n_clicks === 0) {
                return [null, null, 'Click the button to get current date and location information'];
            }
            
            if (!navigator.geolocation) {
                return [null, null, '❌ Geolocation is not supported by this browser'];
            }
            
            return new Promise(function(resolve) {
                navigator.geolocation.getCurrentPosition(
                    function(position) {
                        var latitude = position.coords.latitude;
                        var today = new Date();
                        var startOfYear = new Date(today.getFullYear(), 0, 1);
                        var dayOfYear = Math.floor((today - startOfYear) / (1000 * 60 * 60 * 24)) + 1;
                        
                        var options = { 
                            weekday: 'long', 
                            year: 'numeric', 
                            month: 'long', 
                            day: 'numeric' 
                        };
                        var formattedDate = today.toLocaleDateString('en-US', options);
                        
                        var successMessage = '✅ Location detected! 📍 Latitude: ' + latitude.toFixed(2) + '° 📅 Date: ' + formattedDate + ' (Day ' + dayOfYear + ' of the year)';
                        
                        resolve([latitude, dayOfYear, successMessage]);
                    },
                    function(error) {
                        var errorMessage = '❌ Unable to retrieve your location';
                        switch(error.code) {
                            case error.PERMISSION_DENIED:
                                errorMessage = '❌ Location access denied. Please allow location access in your browser settings and try again.';
                                break;
                            case error.POSITION_UNAVAILABLE:
                                errorMessage = '❌ Location information unavailable. Please check your internet connection and try again.';
                                break;
                            case error.TIMEOUT:
                                errorMessage = '❌ Location request timed out. Please try again.';
                                break;
                        }
                        resolve([null, null, errorMessage]);
                    },
                    {
                        enableHighAccuracy: true,
                        timeout: 15000,
                        maximumAge: 300000
                    }
                );
            });
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