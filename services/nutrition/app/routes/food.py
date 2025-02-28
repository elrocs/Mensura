from typing import Any, Dict, Optional

from app.services.food import FoodService
from flask import Blueprint, jsonify, request
from flask.typing import ResponseReturnValue

food_bp: Blueprint = Blueprint("food", __name__)


@food_bp.route("/foods", methods=["GET"])
def get_foods() -> ResponseReturnValue:
    foods = FoodService.get_all()
    food_list: list[Dict[str, Any]] = [
        {"name": food.name, "calories": food.calories} for food in foods
    ]
    return jsonify({"foods": food_list})


@food_bp.route("/foods", methods=["POST"])
def add_food() -> ResponseReturnValue:
    data: Optional[Dict[str, Any]] = request.json
    if not data:
        return jsonify({"error": "Invalid or missing JSON"}), 400
    try:
        new_food = FoodService.add(data)
        return jsonify({"message": f"Added {new_food.name}"}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@food_bp.route("/foods/<string:name>", methods=["DELETE"])
def delete_food(name: str) -> ResponseReturnValue:
    food = FoodService.remove(name)
    if food:
        return jsonify({"message": f"Deleted {food.name}"}), 200
    return jsonify({"error": "Food"})
