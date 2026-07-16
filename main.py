from database import DatabaseConnection, Session
from fastapi import FastAPI, HTTPException
from repository import RecipeRepository, EssenceRepository, MaterialRepository
from auth import hash_password

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome! Please log in with /login/username,password"}

@app.post("/register")
def register(username: str, password: str):
    session = Session(DatabaseConnection())
    user_repository = UserRepository(session)

    if user_repository.get_by_name(username):
        raise HTTPException(
            status_code=409,
            detail="Username already exists"
        )

    user = AppUser(
        username=username,
        password=hash_password(password)
    )

    user_repository.insert(user)

    return {"message": "User registered successfully"}

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

