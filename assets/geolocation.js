/**
 * Geolocation functionality for Solar Path Visualizer
 * Handles location detection and date calculation
 */

function getCurrentLocationAndDate(n_clicks) {
    if (n_clicks === 0) {
        return [null, null, 'Click the button to get current date and location information'];
    }
    
    if (!navigator.geolocation) {
        return [null, null, '❌ Geolocation is not supported by this browser'];
    }
    
    return new Promise(function(resolve) {
        navigator.geolocation.getCurrentPosition(
            function(position) {
                const latitude = position.coords.latitude;
                const today = new Date();
                const startOfYear = new Date(today.getFullYear(), 0, 1);
                const dayOfYear = Math.floor((today - startOfYear) / (1000 * 60 * 60 * 24)) + 1;
                
                const options = { 
                    weekday: 'long', 
                    year: 'numeric', 
                    month: 'long', 
                    day: 'numeric' 
                };
                const formattedDate = today.toLocaleDateString('en-US', options);
                
                const successMessage = '✅ Location detected! 📍 Latitude: ' + latitude.toFixed(2) + '° 📅 Date: ' + formattedDate + ' (Day ' + dayOfYear + ' of the year)';
                
                resolve([latitude, dayOfYear, successMessage]);
            },
            function(error) {
                let errorMessage = '❌ Unable to retrieve your location';
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