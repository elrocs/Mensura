from flask import Flask
from .food import food_bp
from .plan import plan_bp

def register_routes(app: Flask):
    app.register_blueprint(food_bp)
    app.register_blueprint(plan_bp)
