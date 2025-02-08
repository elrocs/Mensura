from bottle import Bottle, run
from db import initialize_db, close_db

from api.food_api import food_api

# Create an instance of the Bottle application
app = Bottle()

# Route to test the API
@app.route('/')
def index():
    return {"message": "Hello, World!"}

if __name__ == '__main__':
    initialize_db()  # Initialize the database before running the app
    try:
        run(app, host='0.0.0.0', port=5000)
    finally:
        close_db()  # Ensure the database connection is closed when the server stops
