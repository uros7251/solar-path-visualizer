import dash
from layout import create_layout
from callbacks import register_callbacks

# Initialize the Dash app
app = dash.Dash(__name__)

# Set the layout
app.layout = create_layout()

# Register callbacks
register_callbacks(app)

# Enable hot reloading
app.config.suppress_callback_exceptions = True
app.enable_dev_tools(dev_tools_hot_reload=True)

if __name__ == '__main__':
    app.run_server(debug=True) 