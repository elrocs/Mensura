from flask import Blueprint, request, jsonify
from services.plan import PlanService

plan_bp = Blueprint("plan", __name__)

@plan_bp.route('/plan', methods=['GET'])
def get_plans():
    plans = PlanService.get_all()
    plan_list = [{}]
    return 