from peewee import Model, CharField, FloatField, IntegerField
from db import db  # Importing the database from db.py

class BaseModel(Model):
    class Meta:
        database = db  # Using the database configured in db.py

class Food(BaseModel):
    name = CharField(unique=True)
    
    # Macronutrients (per 100g)
    calories = FloatField()
    protein = FloatField()
    carbs = FloatField()
    fats = FloatField()
    fiber = FloatField()
    
    # Micronutrients (all in mg per 100g)
    vitamin_a = FloatField(null=True)  # in mg
    vitamin_c = FloatField(null=True)  # in mg
    vitamin_d = FloatField(null=True)  # in mg
    vitamin_e = FloatField(null=True)  # in mg
    vitamin_k = FloatField(null=True)  # in mg
    calcium = FloatField(null=True)    # in mg
    iron = FloatField(null=True)       # in mg
    magnesium = FloatField(null=True)  # in mg
    potassium = FloatField(null=True)  # in mg
    sodium = FloatField(null=True)     # in mg
    zinc = FloatField(null=True)       # in mg
