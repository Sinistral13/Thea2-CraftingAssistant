from database import DatabaseConnection, Session
from fastapi import FastAPI, HTTPException
from repository import RecipeRepository, EssenceRepository, MaterialRepository

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome!"}

@app.get("/recipes/{recipe_name}")
def get_recipe(recipe_name):
    session = Session(DatabaseConnection())

    recipe_repository = RecipeRepository(session)

    recipe = recipe_repository.get_by_name(recipe_name)

    if recipe is None:
        raise HTTPException(
            status_code=404,
            detail="Recipe not found"
        )

    return recipe
    
#get_recipe("Sword")   