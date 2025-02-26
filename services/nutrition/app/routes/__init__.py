from flask import Flask

def register_routes(app: Flask):
    from app.routes.food import food_bp
    from app.routes.plan import plan_bp

    app.register_blueprint(food_bp)
    app.register_blueprint(plan_bp)