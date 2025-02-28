from typing import Optional

from app.db import close, initialize
from app.routes import register_routes
from flask import Flask

app: Flask = Flask(__name__)


# Initialize the database
initialize()

# Register routes
register_routes(app)


@app.teardown_appcontext
def teardown(exception: Optional[BaseException]) -> None:
    """Close the database connection after each request."""
    close()


if __name__ == "__main__":
    app.run(debug=True)
