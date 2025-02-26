from flask import Blueprint, request, jsonify
from app.services.plan import PlanService

plan_bp = Blueprint("plan", __name__)

@plan_bp.route('/plans', methods=['GET'])
def get_plans():
    plans = PlanService.get_all()
    plan_list = [{"name": plan.name, "price": plan.price} for plan in plans]
    return jsonify({"plans": plan_list})