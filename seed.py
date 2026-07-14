import fdb
import os
from dotenv import load_dotenv


load_dotenv()
DB_PASSWORD = os.getenv('DB_PASSWORD')

if not DB_PASSWORD:
    raise ValueError(
    "DB_PASSWORD not found. Please add your DB_PASSWORD to the .env file."
    )

my_connection = fdb.connect(
    dsn="THEA_MAT",
    user="SYSDBA",
    password=DB_PASSWORD
)

my_cursor = my_connection.cursor()


essences = [
    (0, "None"),
    (1,"wood"),
    (2,"gem"),
    (3,"bone"),
    (4,"leather"),
    (5,"metal"),
    (6, "stone")
    ]

subtypes = [
    (0, "none"),
    (1, "wild"),
    (2, "improved")]

materials = [
    (0, "None", 0, 0, 0, 0, 0, False, 0),
    (1, "Wood", 1, 0.5, 0, 0, 0, False, 0),
    (2, "Elven Wood", 1, 0.9, 0, 0, 2, False, 1),
    (3, "Dryad Wood", 1, 0.9, 0, 0, 0, False, 1),
    (4, "Dark Wood", 1, 1.1, 0, 0, 1, False, 1),
    (5, "Ancient Wood", 1, 1.4, 0, 0, 0, False, 2),
    (6, "Crystal Wood", 1, 1.6, 2, 1.3, 1, True, 3),
    (7, "Sacred Wood", 1, 2.4, 0, 0, 0, False, 3),
    (8, "Stone Wood", 1, 1.1, 6, 1.3, 2, True, 3),
    (9, "Life Root", 1, 2.0, 2, 1.6, 2, True, 4),
    (10, "God's Branch", 1, 2.4, 6, 1.9, 1, True, 4),
    (11, "Amber", 2, 0.5, 0, 0, 0, False, 0),
    (12, "Topaz", 2, 0.9, 0, 0, 2, False, 1),
    (13, "Malachite", 2, 0.9, 0, 0, 0, False, 1),
    (14, "Ruby", 2, 1.1, 0, 0, 1, False, 1),
    (15, "Diamond", 2, 1.4, 0, 0, 0, False, 2),
    (16, "Grandgem", 2, 2.4, 0, 0, 0, False, 3),
    (17, "Earth Core", 2, 2.4, 1, 1.9, 1, True, 4),
    (18, "Void Sparkler", 2, 2.0, 3, 1.6, 2, True, 4),
    (19,"Bone", 3, 0.5, 0, 0, 0, False, 0),
    (20, "Blood Bone", 3, 0.9, 0, 0, 2, False, 1),
    (21, "Monster Bone", 3, 0.9, 0, 0, 0, False, 1),
    (22, "Shadow Bone", 3, 1.1, 0, 0, 1, False, 1),
    (23, "Dragon Bone", 3, 1.4, 0, 0, 0, False, 2),
    (24, "Enchanted Bone", 3, 1.1, 2, 1.3, 2, True, 3),
    (25, "Rune Bone", 3, 2.4, 0, 0, 0, False, 3),
    (26, "Forgotten Essence", 3, 2.4, 2, 1.9, 1, True, 4),
    (27, "Leather", 4, 0.5, 0, 0, 0, False, 0),
    (28, "Scaled Leather", 4, 0.9, 0, 0, 2, False, 1),
    (29, "Fur Leather", 4, 0.9, 0, 0, 0, False, 1),
    (30, "Enchanted Leather", 4, 1.1, 0, 0, 1, False, 1),
    (31, "Mythical Leather", 4, 1.4, 0, 0, 0, False, 2),
    (32, "Spike Leather", 4, 1.3, 3, 1.6, 1, True, 3),
    (33, "Combat Leather", 4, 2.4, 0, 0, 0, False, 3),
    (34, "Golem Leather", 4, 1.3, 5, 1.1, 2, True, 3),
    (35, "Morph Material", 4, 2.4, 3, 1.9, 1, True, 4),
    (36, "Alchemy Skin", 4, 2.0, 5, 1.6, 2, True, 4),
    (37, "Iron", 5, 0.5, 0, 0, 0, False, 0),
    (38, "Silver", 5, 0.9, 0, 0, 2, False, 1),
    (39, "Steel", 5, 0.9, 0, 0, 0, False, 1),
    (40, "Gold", 5, 1.1, 0, 0, 1, False, 1),
    (41, "Mithril", 5, 1.4, 0, 0, 0, False, 2),
    (42, "Metal Composite", 5, 2.4, 0, 0, 0, False, 3),
    (43, "Igneous Spike", 5, 2.4, 4, 1.9, 1, True, 4),
    (44, "Secret Alloy", 5, 2.0, 6, 1.6, 2, True, 4),
    (45, "Sandstone", 6, 0.5, 0, 0, 0, False, 0),
    (46, "Granite", 6, 1.1, 0, 0, 1, False, 1),
    (47, "Clay", 6, 0.9, 0, 0, 0, False, 1),
    (48, "Quartz", 6, 0.9, 0, 0, 2, False, 1),
    (49, "Obsidian", 6, 1.4, 0, 0, 0, False, 2),
    (50, "Armoured Stone", 6, 1.3, 5, 1.6, 1, True, 3),
    (51, "Pure Stone", 6, 2.4, 0, 0, 0, False, 3),
    (52, "Moonstone", 6, 2.4, 5, 1.9, 1, True, 4),
    (53, "Pristine Matter", 6, 2.0, 1, 1.6, 2, True, 4),
]

recipes = [
    (0,"Sword",10,5,14,5,12,6,11,3,7,6,10,3,9,3,8,4),
    (1,"Greatsword",20,1,18,6,25,5,23,3,16,2,14,4,12,3,18,5),
    (2,"Hatchet",14,6,12,5,11,3,10,6,10,5,9,4,8,6,7,5),
    (3,"Battle Axe",23,3,20,5,18,6,25,6,14,4,12,5,18,5,16,6),
    (4,"Club",10,2,14,6,12,5,11,1,8,1,7,4,10,5,9,6),
    (5,"Mallet",23,5,20,1,18,2,25,6,12,1,18,5,16,6,14,3),
    (6,"Bow",10,5,14,1,12,3,11,2,10,4,9,5,8,3,7,1),
    (7,"Wand",10,3,14,3,12,1,11,2,10,5,9,1,8,6,7,5),
    (8,"Javelin",25,6,23,5,20,3,18,6,14,6,12,3,18,3,16,5),
    (9,"Shield",18,3,16,5,14,1,20,1,14,1,13,3,11,4,10,2),
    (10,"Jewellery",12,5,18,2,16,3,14,4,11,4,10,2,8,1,12,6),
    (11,"Leather Robes",13,4,12,2,16,4,15,2,8,1,7,3,10,4,9,2),
    (12,"Medium Armor",27,1,24,5,22,3,30,4,12,6,16,4,15,1,13,5),
    (13,"Heavy Armor",30,3,42,5,38,6,34,1,23,1,20,4,18,2,25,1),
    (14,"Spear",10,2,14,6,12,3,11,6,5,1,7,4,10,5,9,2),
    (15,"Polearm",23,6,20,1,18,5,25,5,18,1,16,2,14,4,12,1),
    (16,"Scroll",12,1,11,2,10,4,14,4,9,3,8,2,7,4,10,4),
    (17,"Codex",18,4,25,4,23,2,20,1,16,2,14,3,12,4,18,4),
    (18,"Artefact",10,1,14,4,12,2,11,3,7,4,10,4,9,5,8,6),
    (19,"Relic",23,2,20,5,18,6,25,6,18,4,16,3,14,2,12,4),
    
]

inventory = [(0,"test",39,12),
             (1,"test",19,15),
             (2,"test",20,2),
             (3,"hacker",13,25),
]

sql_essence = "INSERT INTO essence VALUES (?, ?)"

for row in essences:
    my_cursor.execute(sql_essence, row)

print("All essences inserted.")
    

sql_subtype = "INSERT INTO subtype VALUES (?, ?)"

for row in subtypes:
    my_cursor.execute(sql_subtype, row)

print("All subtypes inserted.")
    

sql_materials = """
INSERT INTO material
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
"""

for row in materials:
    my_cursor.execute(sql_materials, row)
    
print("All materials inserted.")


sql_recipes = """
INSERT INTO recipe
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
"""

for row in recipes:
    my_cursor.execute(sql_recipes, row)
    
print("All recipes inserted.")


sql_inventory = """
INSERT INTO inventory
VALUES (?, ?, ?, ?)
"""

for row in inventory:
    my_cursor.execute(sql_inventory, row)
    
print("Inventory inserted.")


print("Seed complete: all data inserted.")


# Restart identity columns
my_cursor.execute("""
    ALTER TABLE essence
    ALTER COLUMN id RESTART WITH 7
""")

my_cursor.execute("""
    ALTER TABLE subtype
    ALTER COLUMN id RESTART WITH 3
""")

my_cursor.execute("""
    ALTER TABLE material
    ALTER COLUMN id RESTART WITH 54
""")

my_cursor.execute("""
    ALTER TABLE recipe
    ALTER COLUMN id RESTART WITH 20
""")

print("Id's restarted.")


my_connection.commit()
my_cursor.close()
my_connection.close()
