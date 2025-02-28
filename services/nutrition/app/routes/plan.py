from typing import Any, Dict, List

from app.services.plan import PlanService
from flask import Blueprint, jsonify
from flask.typing import ResponseReturnValue

plan_bp: Blueprint = Blueprint("plan", __name__)


@plan_bp.route("/plans", methods=["GET"])
def get_plans() -> ResponseReturnValue:
    plans = PlanService.get_all()
    plan_list: List[Dict[str, Any]] = [
        {"name": plan.name, "price": plan.price} for plan in plans
    ]
    return jsonify({"plans": plan_list})
