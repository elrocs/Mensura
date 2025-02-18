from peewee import SqliteDatabase

DATABASE = 'database.db'
db = SqliteDatabase(DATABASE)

def initialize_db():
    """
    Connects to the database and creates the necessary tables if they don't exist.
    """
    from models import Food

    db.connect()
    db.create_tables([Food], safe=True)  # safe=True prevents an error if the table already exists
    print("Database initialized.")

def close_db():
    """
    Closes the connection to the database.
    """
    db.close()
