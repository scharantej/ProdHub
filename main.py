
# Import Flask
from flask import Flask, render_template

# Create a Flask app
app = Flask(__name__)

# Define the route for the landing page
@app.route('/')
def index():
    """Render the landing page."""
    return render_template('index.html')

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
