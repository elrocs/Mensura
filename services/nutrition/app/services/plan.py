from typing import List, Optional

from app.models.plan import Plan


class PlanService:
    @staticmethod
    def get_all() -> List[Plan]:
        """Fetch all nutrition plans from the database."""
        return list(Plan.select())

    @staticmethod
    def get(name: str) -> Optional[Plan]:
        """Fetch a nutrition plan from the database."""
        return Plan.get_or_none(Plan.name == name.lower())

    @staticmethod
    def remove(name: str) -> Optional[Plan]:
        """Remove a nutrition plan from the database by name."""
        plan = Plan.get_or_none(Plan.name == name.lower())
        if plan:
            plan.delete_instance(recursive=True)
            return plan
        return None
