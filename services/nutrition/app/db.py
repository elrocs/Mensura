import os

from peewee import SqliteDatabase

# Database configuration
db_path = os.path.join(os.path.dirname(__file__), "data/nutrition.db")
os.makedirs(os.path.dirname(db_path), exist_ok=True)
db = SqliteDatabase(db_path)


def initialize():
    """Connect and create tables if they don't exist."""

    from app.models.food import Food
    from app.models.plan import Plan, PlanItem

    ALL_MODELS = [Food, Plan, PlanItem]

    try:
        db.connect()
        db.create_tables(ALL_MODELS, safe=True)
    except Exception as e:
        print(f"Database initialization failed: {e}")
    finally:
        db.close()


def close():
    """Close the database connection."""
    if not db.is_closed():
        db.close()
