from peewee import SqliteDatabase
from models.food import Food
from flask import current_app

# Database configuration
db = SqliteDatabase(current_app.config['DATABASE'])

def initialize():
    """Connect and create tables if they don't exist."""
    db.connect()
    db.create_tables([Food], safe=True)  # safe=True prevents table creation if it already exists

def close():
    """Close the database connection."""
    db.close()
