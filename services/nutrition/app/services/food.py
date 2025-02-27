from app.models.food import Food
from peewee import IntegrityError


class FoodService:
    @staticmethod
    def get_all():
        """Fetch all food items from the database."""
        return Food.select()

    @staticmethod
    def add(data):
        """Add a new food item to the database."""
        try:
            new_food = Food.create(
                name=data["name"].lower(),
                calories=data["calories"],
                protein=data["protein"],
                carbs=data["carbs"],
                fats=data["fats"],
                fiber=data["fiber"],
                vitamin_a=data.get("vitamin_a"),
                vitamin_c=data.get("vitamin_c"),
                vitamin_d=data.get("vitamin_d"),
                vitamin_e=data.get("vitamin_e"),
                vitamin_k=data.get("vitamin_k"),
                calcium=data.get("calcium"),
                iron=data.get("iron"),
                magnesium=data.get("magnesium"),
                potassium=data.get("potassium"),
                sodium=data.get("sodium"),
                zinc=data.get("zinc"),
            )
            return new_food
        except IntegrityError:
            raise ValueError("Food with this name already exists")

    @staticmethod
    def remove(name):
        """Remove a food item from the database by name."""
        food_item = Food.get_or_none(Food.name == name.lower())
        if food_item:
            food_item.delete_instance()
            return food_item
        return None

    @staticmethod
    def update(name, data):
        """Update a food item with new data."""
        food_item = Food.get_or_none(Food.name == name.lower())
        if food_item:
            for field, value in data.items():
                if hasattr(food_item, field):
                    setattr(food_item, field, value)
            food_item.save()
            return food_item
        return None
