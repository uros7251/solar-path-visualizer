import dash
from layout import create_layout
from callbacks import register_callbacks
import os

# Initialize the Dash app
app = dash.Dash(__name__)

# Set the external HTML template
try:
    template_path = os.path.join(os.path.dirname(__file__), 'templates', 'index.html')
    app.index_string = open(template_path, 'r', encoding='utf-8').read()
except FileNotFoundError:
    print("Warning: templates/index.html not found. Using default template.")
except Exception as e:
    print(f"Warning: Could not load custom template: {e}. Using default template.")

# Set the layout
app.layout = create_layout()

# Register callbacks
register_callbacks(app)

# Enable hot reloading
app.config.suppress_callback_exceptions = True
app.enable_dev_tools(dev_tools_hot_reload=True)

if __name__ == '__main__':
    app.run_server(debug=True) 