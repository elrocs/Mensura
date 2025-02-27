from flask import Blueprint, jsonify, request

from app.services.food import FoodService

food_bp = Blueprint("food", __name__)


@food_bp.route("/foods", methods=["GET"])
def get_foods():
    foods = FoodService.get_all()
    food_list = [{"name": food.name, "calories": food.calories} for food in foods]
    return jsonify({"foods": food_list})


@food_bp.route("/foods", methods=["POST"])
def add_food():
    data = request.json
    if not data:
        return jsonify({"error": "Invalid or missing JSON"}), 400
    try:
        new_food = FoodService.add(data)
        return jsonify({"message": f"Added {new_food.name}"}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@food_bp.route("/foods/<string:name>", methods=["DELETE"])
def delete_food(name):
    food = FoodService.remove(name)
    if food:
        return jsonify({"message": f"Deleted {food.name}"}), 200
    return jsonify({"error": "Food not found"}), 404


@food_bp.route("/foods/<string:name>", methods=["PUT"])
def update_food(name):
    data = request.json
    if not data:
        return jsonify({"error": "Invalid or missing JSON"}), 400
    updated_food = FoodService.update(name, data)
    if updated_food:
        return jsonify({"message": f"Updated {updated_food.name}"}), 200
    return jsonify({"error": "Food not found"}), 404
