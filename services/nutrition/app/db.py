from peewee import SqliteDatabase
import os

# Database configuration
db_path = os.path.join(os.path.dirname(__file__), 'data/nutrition.db')
os.makedirs(os.path.dirname(db_path), exist_ok=True)
db = SqliteDatabase(db_path)


def initialize():
    """Connect and create tables if they don't exist."""
    from models.food import Food
    db.connect()
    db.create_tables([Food], safe=True)  # safe=True prevents table creation if it already exists

def close():
    """Close the database connection."""
    db.close()
