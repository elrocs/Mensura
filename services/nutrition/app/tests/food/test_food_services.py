import pytest
from app.models.food import Food
from app.services.food import FoodService
from playhouse.sqlite_ext import SqliteExtDatabase

# In-memory test database
test_db = SqliteExtDatabase(":memory:")

@pytest.fixture(scope="function", autouse=True)
def setup_database():
    """Sets up an in-memory database before each test."""
    test_db.bind([Food], bind_refs=False, bind_backrefs=False)
    test_db.connect()
    test_db.create_tables([Food])
    yield
    test_db.drop_tables([Food])
    test_db.close()

def test_get_all_empty():
    """Ensure get_all() returns an empty list when there are no food items."""
    assert FoodService.get_all() == []

def test_get_all_with_data():
    """Ensure get_all() returns all food items."""
    Food.create(name="apple", calories=95, protein=0.3, carbs=25, fats=0.2, fiber=4)
    Food.create(name="banana", calories=105, protein=1.3, carbs=27, fats=0.3, fiber=3)

    foods = FoodService.get_all()
    assert len(foods) == 2
    assert foods[0].name == "apple"
    assert foods[1].name == "banana"

def test_add_food():
    """Ensure add() correctly inserts a new food item."""
    data = {
        "name": "orange",
        "calories": 62,
        "protein": 1.2,
        "carbs": 15,
        "fats": 0.2,
        "fiber": 3.1
    }
    food = FoodService.add(data)

    assert food.name == "orange"
    assert food.calories == 62
    assert Food.select().count() == 1

def test_add_duplicate_food():
    """Ensure add() raises an error when trying to insert a duplicate food item."""
    data = {"name": "grape", "calories": 67, "protein": 0.6, "carbs": 17, "fats": 0.4, "fiber": 0.9}
    FoodService.add(data)  # First insertion should pass

    with pytest.raises(ValueError, match="Food with this name already exists"):
        FoodService.add(data)  # Second insertion should fail

def test_remove_existing_food():
    """Ensure remove() deletes an existing food item."""
    Food.create(name="kiwi", calories=42, protein=0.8, carbs=10, fats=0.4, fiber=2.1)
    deleted_food = FoodService.remove("kiwi")

    assert deleted_food is not None
    assert deleted_food.name == "kiwi"
    assert Food.select().count() == 0

def test_remove_nonexistent_food():
    """Ensure remove() returns None when trying to delete a non-existing food item."""
    assert FoodService.remove("mango") is None

def test_update_existing_food():
    """Ensure update() modifies an existing food item."""
    Food.create(name="peach", calories=59, protein=1, carbs=14, fats=0.4, fiber=2)

    updated_food = FoodService.update("peach", {"calories": 50, "fiber": 3})

    assert updated_food is not None
    assert updated_food.calories == 50
    assert updated_food.fiber == 3

def test_update_nonexistent_food():
    """Ensure update() returns None when trying to modify a non-existing food item."""
    assert FoodService.update("watermelon", {"calories": 30}) is None
