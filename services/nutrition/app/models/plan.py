from peewee import Model, CharField, FloatField, DateTimeField
from peewee import ForeignKeyField
from db import db

class Plan(Model):
    name = CharField(unique= True)
    created_at = DateTimeField(default=datetime.now)

    class Meta:
        database = db

class PlanItem():
    plan = ForeignKeyField(Plan, backref="items", on_delete"CASCADE")
    food = ForeignKeyField(Food, backref="plans")
    quantity = FloatField() # g or ml

    class Meta:
        database = db
