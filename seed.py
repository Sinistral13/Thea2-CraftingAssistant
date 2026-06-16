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

sql_essence = "INSERT INTO essence VALUES (?,?)"

for row in essences:
    my_cursor.execute(sql_essence, row)

print("All essences inserted.")
    

sql_subtype = "INSERT INTO subtype VALUES (?,?)"

for row in subtypes:
    my_cursor.execute(sql_subtype, row)

print("All sybtypes inserted.")
    

sql = """
INSERT INTO material
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
"""

for row in materials:
    my_cursor.execute(sql, row)
    
print("All materials inserted.")

my_connection.commit()
my_cursor.close()
my_connection.close()

print("Seed complete: all data inserted.")