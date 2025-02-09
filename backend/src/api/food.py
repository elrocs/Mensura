from bottle import Bottle, request, response  # Importing necessary modules from Bottle framework
from peewee import IntegrityError  # Importing IntegrityError from peewee to handle duplicate entries
from models import Food  # Importing the Food model from models.py

# Create an instance of Bottle to handle our application
food = Bottle()

# Define a GET route for retrieving all food items
@food.get('/')
def get_food():
    foods = Food.select()  # Retrieve all food entries from the database

    food_list = []  # List to store the food data for the response
    for food_item in foods:
        # For each food item, extract its properties and store them in the food_list
        food_list.append({
            "name": food_item.name,
            "calories": food_item.calories,
            "protein": food_item.protein,
            "carbs": food_item.carbs,
            "fats": food_item.fats,
            "fiber": food_item.fiber,
            "vitamin_a": food_item.vitamin_a,
            "vitamin_c": food_item.vitamin_c,
            "vitamin_d": food_item.vitamin_d,
            "vitamin_e": food_item.vitamin_e,
            "vitamin_k": food_item.vitamin_k,
            "calcium": food_item.calcium,
            "iron": food_item.iron,
            "magnesium": food_item.magnesium,
            "potassium": food_item.potassium,
            "sodium": food_item.sodium,
            "zinc": food_item.zinc
        })
    
    response.content_type = 'application/json'  # Set the response type to JSON
    return {"foods": food_list}  # Return the food list as a JSON object

# Define a POST route to add a new food item
@food.post('/add')
def add_food():
    data = request.json  # Parse the JSON data from the request body
    
    # Check if the data is missing or invalid
    if not data:
        response.status = 400  # Set HTTP status to 400 for bad request
        return {"error": "Invalid or missing JSON"}

    try:
        # Create a new food entry in the database with the data provided
        new_food = Food.create(
            name=data["name"].lower(),  # Ensure food name is saved in lowercase
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
            zinc=data.get("zinc")
        )

        response.status = 201  # Set HTTP status to 201 for resource creation
        return {"message": f"Added {new_food.name}"}  # Return a success message

    except IntegrityError:
        # This exception is raised if there is a duplicate food name (unique constraint violation)
        response.status = 400  # Set HTTP status to 400 for bad request
        return {"error": "Food with this name already exists"}
    
    except KeyError as e:
        # This exception is raised if a required field is missing in the request
        response.status = 400  # Set HTTP status to 400 for bad request
        return {"error": f"Missing required field: {str(e)}"}  # Return the name of the missing field

# Define a DELETE route to remove a food item by its name
@food.delete('/remove')
def remove_food():
    food_name = request.query.get('name').lower()  # Get the food name from the query parameter and convert to lowercase

    # Search for the food item in the database
    food_item = Food.get_or_none(Food.name == food_name)

    if food_item:
        food_item.delete_instance()  # If food item is found, delete it from the database
        response.status = 200  # Set HTTP status to 200 for successful request
        return {"message": f"Food '{food_name}' has been removed successfully."}  # Return a success message
    else:
        response.status = 404  # Set HTTP status to 404 for not found
        return {"message": f"Food '{food_name}' not found."}  # Return an error message if food item is not found

@food.patch('/update')
def update_food():
    food_name = request.query.get('name').lower()  # Get the food name to update
    data = request.json  # Get the JSON data from the request

    # Search for the food item by its name
    food_item = Food.get_or_none(Food.name == food_name)

    # If the food item exists
    if food_item:
        # Only update the fields that are sent in the request
        if "calories" in data:
            food_item.calories = data["calories"]
        if "protein" in data:
            food_item.protein = data["protein"]
        if "carbs" in data:
            food_item.carbs = data["carbs"]
        if "fats" in data:
            food_item.fats = data["fats"]
        if "fiber" in data:
            food_item.fiber = data["fiber"]
        if "vitamin_a" in data:
            food_item.vitamin_a = data.get("vitamin_a")
        if "vitamin_c" in data:
            food_item.vitamin_c = data.get("vitamin_c")
        if "vitamin_d" in data:
            food_item.vitamin_d = data.get("vitamin_d")
        if "vitamin_e" in data:
            food_item.vitamin_e = data.get("vitamin_e")
        if "vitamin_k" in data:
            food_item.vitamin_k = data.get("vitamin_k")
        if "calcium" in data:
            food_item.calcium = data.get("calcium")
        if "iron" in data:
            food_item.iron = data.get("iron")
        if "magnesium" in data:
            food_item.magnesium = data.get("magnesium")
        if "potassium" in data:
            food_item.potassium = data.get("potassium")
        if "sodium" in data:
            food_item.sodium = data.get("sodium")
        if "zinc" in data:
            food_item.zinc = data.get("zinc")
        
        # Save the updated food item to the database
        food_item.save()

        response.status = 200  # Success status code
        return {"message": f"Food '{food_name}' updated successfully."}  # Success message
    else:
        response.status = 404  # If the food item is not found
        return {"message": f"Food '{food_name}' not found."}  # Error message if food item is not found
