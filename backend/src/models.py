from peewee import Model, CharField, FloatField
from db import db  # Importing the database from db.py

class BaseModel(Model):
    class Meta:
        database = db  # Using the database configured in db.py

class Food(BaseModel):
    name = CharField(unique=True)

    # Macronutrients in mg per 100g
    calories = FloatField()   # Remains in kcal
    protein = FloatField()    # mg
    carbs = FloatField()      # mg
    fats = FloatField()       # mg
    fiber = FloatField()      # mg

    # Micronutrients (mg or µg as appropriate)
    vitamin_a = FloatField(null=True)  # µg (micrograms)
    vitamin_c = FloatField(null=True)  # mg
    vitamin_d = FloatField(null=True)  # µg
    vitamin_e = FloatField(null=True)  # mg
    vitamin_k = FloatField(null=True)  # µg
    calcium = FloatField(null=True)    # mg
    iron = FloatField(null=True)       # mg
    magnesium = FloatField(null=True)  # mg
    potassium = FloatField(null=True)  # mg
    sodium = FloatField(null=True)     # mg
    zinc = FloatField(null=True)       # mg
