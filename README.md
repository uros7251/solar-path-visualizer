# Solar Path Visualizer

An interactive web application that visualizes the sun's movement across the sky for any given latitude and day of the year. Built with Dash and Plotly.

## Features

- Interactive visualization of sun path
- Time series plot showing altitude and azimuth over time
- Polar projection of the sun's path
- Adjustable latitude (-90° to 90°)
- Day of year selection with month markers
- Real-time solar declination display
- Automatic location and date detection using browser geolocation

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/solar-path-visualizer.git
cd solar-path-visualizer
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the application:
```bash
python app.py
```

Then open your browser and navigate to `http://127.0.0.1:8050/`

### Location Detection Feature

1. Click the "Get Current Date & Location Info" button
2. Allow location access when prompted by your browser
3. The application will automatically:
   - Detect your current latitude
   - Get the current date
   - Update both latitude and day-of-year sliders
   - Show the solar path for your exact location and current date

## Project Structure

```
solar-path-visualizer/
├── app.py              # Main application entry point
├── callbacks.py        # Dash callbacks for interactivity
├── constants.py        # Color scheme and solar constants
├── layout.py          # Application layout and styling
├── sun_calculations.py # Solar position calculations
├── plots/             # Plotting modules
│   ├── time_series.py # Time series plot
│   └── polar.py       # Polar projection plot
├── templates/         # HTML templates
│   └── index.html     # Custom HTML template
├── assets/            # Static assets
│   ├── custom.css     # Custom CSS styles
│   ├── geolocation.js # Location detection JavaScript
│   └── plotly-resize.js # Plotly resize functionality
├── requirements.txt    # Project dependencies
└── README.md          # This file
```

## Dependencies

- dash==2.14.2
- plotly==5.18.0
- numpy==1.26.3
- matplotlib==3.10.3
- dash-latex==0.1.0

## Browser Compatibility

The location detection feature requires a modern browser with geolocation support. The application will gracefully handle cases where:
- Geolocation is not supported
- Location access is denied
- Network connectivity issues occur

## License

MIT License 