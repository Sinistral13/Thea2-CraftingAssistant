from database import DatabaseConnection, Session
from models import Recipe, Material, Subtype, Essence 


def main():

    database = DatabaseConnection()

    session = Session(database)

    print("Test Recipe")
    #Test 1: get id =5 --> name = 'Mallet'.
    recipe =  session.recipes.get_by_id(5)

    print(f"Test1: {recipe.name == 'Mallet'} ")
    
    
    #Test 2: get name = 'Sword"' --> id = 0.
    recipe =  session.recipes.get_by_name("Sword")

    
    print(f"Test2: {recipe.id == 0} ")
    
    #Test3, get all
    recipes = session.recipes.get_all()
    print(f"Test3: {len(recipes) > 0}")

    #Test4, mapping
    r1 = session.recipes.get_by_id(5)
    r2 = session.recipes.get_by_id(5)
    print(f"Test4: {r1 is r2}")
    
    #Test5, insert
    recipe = Recipe(
    id=None,
    name="insertTest",
    primary_amount1=1,
    primary_essence_id1=1,
    primary_amount2=2,
    primary_essence_id2=2,
    primary_amount3=3,
    primary_essence_id3=3,
    primary_amount4=4,
    primary_essence_id4=4,
    secondary_amount1=1,
    secondary_essence_id1=1,
    secondary_amount2=2,
    secondary_essence_id2=2,
    secondary_amount3=3,
    secondary_essence_id3=3,
    secondary_amount4=4,
    secondary_essence_id4=4,
    )

    new_id = session.recipes.insert(recipe)

    saved = session.recipes.get_by_id(new_id)

    print(f"Test5a: {saved is not None}")
    print(f"Test5b: {saved.name == 'insertTest'}")
    print(f"Test5c: {saved.primary_amount1 == 1}")
    print(f"Test5d: {saved.secondary_essence_id4 == 4}")
    
    session.recipes.delete_by_id(new_id)
    print(f"Test5e: {session.recipes.get_by_id(new_id) is None}")
    
    database.close()


if __name__ == "__main__":
    main()