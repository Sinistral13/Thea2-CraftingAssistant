from database import DatabaseConnection, Session
from models import Recipe, Material, Subtype, Essence 


def main():

    database = DatabaseConnection()

    session = Session(database)

    print("Test Material")
    #Test 1a: get id = 11 --> name = 'Amber'.
    material =  session.materials.get_by_id(11)

    print(f"Test1a: {material.name == 'Amber'} ")
    
    #Test 1b: get id = 102 --> name = ''.
    material =  session.materials.get_by_id(102)

    print(f"Test1b: {material is None} ")
    
     #Test 2a: get name = 'Silver' --> id = 38.
    material =  session.materials.get_by_name("Silver")

    print(f"Test2a: {material.id == 38} ")
    
    #Test 2b: get name = 'Test' --> id = None.
    material =  session.materials.get_by_name("Test")

    print(f"Test2b: {material is None} ")
    
    
    #Test3, get all
    materials = session.materials.get_all()
    print(f"Test3: {len(materials) > 0}")

    #Test4, mapping
    r1 = session.materials.get_by_id(5)
    r2 = session.materials.get_by_id(5)
    print(f"Test4: {r1 is r2}")
    
    #Test5, insert
    material = Material(
    id=None,
    name="insertTest",
    essence1_id=1,
    amount1=10,
    essence2_id=0,
    amount2=0,
    subtype_id=1,
    composite=False,
    tier=2
    )

    new_id = session.materials.insert(material)

    saved = session.materials.get_by_id(new_id)

    print(f"Test5a: {saved is not None}")
    print(f"Test5b: {saved.name == 'insertTest'}")
    print(f"Test5c: {saved.amount1 == 10}")
    print(f"Test5d: {saved.composite == False}")
    
    session.materials.delete_by_id(new_id)
    print(f"Test5e: {session.materials.get_by_id(new_id) is None}")
    
    
    #Test6, faulty insert, id is already in DB, insert still goes through because repo handles it per trigger
    material = Material(
    id=9,
    name="insertTest4",
    essence1_id=1,
    amount1=10,
    essence2_id=0,
    amount2=0,
    subtype_id=1,
    composite=False,
    tier=2
    )

    new_id = session.materials.insert(material)
    saved = session.materials.get_by_id(new_id)
    print(f"Test6a: {saved is not None}")
    session.materials.delete_by_id(new_id)
    
    
    
    
    
    
        
    database.close()
    

if __name__ == "__main__":
    main()