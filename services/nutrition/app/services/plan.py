from app.models.plan import Plan


class PlanService:
    @staticmethod
    def get_all():
        """Fetch all nutrition plans from the database."""
        return Plan.select()

    @staticmethod
    def get():
        """Fetch a nutrition plan from the database."""
        return Plan.get_or_none(Plan.name == name.lower())

    @staticmethod
    def remove():
        """Remove a nutrition plan from the database by name."""
        plan = Plan.get_or_none(Plan.name == name.lower())
        if plan:
            plan.delete_instance(recursive=True)
            return plan
        return None
