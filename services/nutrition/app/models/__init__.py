from .food import Food
from playhouse.sqlite_ext import SqliteExtDatabase

# Initialize the database connection here if needed
db = SqliteExtDatabase('food.db')
