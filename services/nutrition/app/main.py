from flask import Flask
from routes import register_routes
from db import initialize, close

app = Flask(__name__)

# Load configuration
app.config.from_pyfile('config.py')

# Initialize the database
initialize()

# Register routes
register_routes(app)

@app.teardown_appcontext
def teardown(exception):
    """Close the database connection after each request."""
    close()

if __name__ == '__main__':
    app.run(debug=True)
