from database import DatabaseConnection, Session
from fastapi import FastAPI, HTTPException, Depends
from repository import RecipeRepository, EssenceRepository, MaterialRepository, UserRepository, InventoryRepository
from authentification import hash_password, create_token, verify_password, get_current_user
from models import AppUser
import craft

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome! Please log in."}

@app.post("/register")
def register(username, password):
    session = Session(DatabaseConnection())

    if session.users.get_by_name(username):
        raise HTTPException(
            status_code=409,
            detail="Username already exists"
        )

    user = AppUser(
        username=username,
        password=hash_password(password)
    )

    session.users.insert(user)

    return {"message": "User registered successfully"}


@app.post("/login")
def login(username, password):
    session = Session(DatabaseConnection())

    user = session.users.get_by_name(username)

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    if not verify_password(password, user.password):
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    token = create_token(username)

    return {
        "access_token": token,
        "token_type": "bearer"
    }

@app.get("/recipes/{recipe_name}")
def get_recipe(recipe_name, token):
    username = get_current_user(token)
    
    session = Session(DatabaseConnection())

    recipe_repository = RecipeRepository(session)

    recipe = recipe_repository.get_by_name(recipe_name)

    if recipe is None:
        raise HTTPException(
            status_code=404,
            detail="Recipe not found"
        )

    return recipe

@app.get("/inventory")
def get_inventory(token):
    username = get_current_user(token)
    
    session = Session(DatabaseConnection())

    inventory_repository = InventoryRepository(session)

    inventory = inventory_repository.get_by_player(username)

    if inventory is None:
        raise HTTPException(
            status_code=404,
            detail="No inventory for this player."
        )

    return inventory


@app.get("/craft")
def get_inventory(player, token):
    username = get_current_user(token)
    
    session = Session(DatabaseConnection())

    inventory_repository = RecipeRepository(session)

    inventory = inventory_repository.get_by_get_by_player(player)

    if inventory is None:
        raise HTTPException(
            status_code=404,
            detail="No inventory for this player."
        )

    return inventory