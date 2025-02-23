from peewee import Model, CharField, IntegerField, FloatField
from playhouse.sqlite_ext import SqliteExtDatabase
from db import db

class Food(Model):
    name = CharField(unique=True)
    calories = IntegerField()
    protein = FloatField()
    carbs = FloatField()
    fats = FloatField()
    fiber = FloatField()
    vitamin_a = FloatField(null=True)
    vitamin_c = FloatField(null=True)
    vitamin_d = FloatField(null=True)
    vitamin_e = FloatField(null=True)
    vitamin_k = FloatField(null=True)
    calcium = FloatField(null=True)
    iron = FloatField(null=True)
    magnesium = FloatField(null=True)
    potassium = FloatField(null=True)
    sodium = FloatField(null=True)
    zinc = FloatField(null=True)

    class Meta:
        database = db  # Tell Peewee to use this database
