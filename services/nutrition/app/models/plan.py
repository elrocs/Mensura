from datetime import datetime

from peewee import CharField, DateTimeField, FloatField, ForeignKeyField, Model

from app.db import db

from . import Food


class Plan(Model):
    name = CharField(unique=True)
    price = FloatField()
    created_at = DateTimeField(default=datetime.now)

    class Meta:
        database = db


class PlanItem(Model):
    plan = ForeignKeyField(Plan, backref="items", on_delete="CASCADE")
    food = ForeignKeyField(Food, backref="plans")
    quantity = FloatField()  # g or ml

    class Meta:
        database = db
