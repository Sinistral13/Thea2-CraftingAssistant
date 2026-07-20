from repository import RecipeRepository, MaterialRepository, InventoryRepository
from database import DatabaseConnection, Session

def get_primary_essences(recipe):
    requirements = [
        (
            recipe.primary_essence_id1,
            recipe.primary_amount1
        ),
        (
            recipe.primary_essence_id2,
            recipe.primary_amount2
        ),
        (
            recipe.primary_essence_id3,
            recipe.primary_amount3
        ),
        (
            recipe.primary_essence_id4,
            recipe.primary_amount4
        ),
    ]
    
    return requirements
    

def get_secondary_essences(recipe):
    requirements = [
        (
            recipe.secondary_essence_id1,
            recipe.secondary_amount1
        ),
        (
            recipe.secondary_essence_id2,
            recipe.secondary_amount2
        ),
        (
            recipe.secondary_essence_id3,
            recipe.secondary_amount3
        ),
        (
            recipe.secondary_essence_id4,
            recipe.secondary_amount4
        ),
    ]
    
    return requirements


def get_inventory_essences(player):

    inventory = session.inventory.get_by_player(player)

    essences = []

    for item in inventory:

        material = session.materials.get_by_id(item.material)

        if material is None:
            continue

        if material.essence1_id is not None:
            essences.append(
                (
                    material.id,
                    material.essence1_id,
                    material.amount1 * item.amount
                )
            )

        if material.essence2_id is not None:
            essences.append(
                (
                    material.id,
                    material.essence2_id,
                    material.amount2 * item.amount
                )
            )

    return essences


def crafting(recipe, player):
    """Check recipe requierements and invenory.
    Create a lists for primary requirements andd a list for the seconddary.
    Return the a touple of those lists.
    If one requirement is not ment return an empty touple."""
    primary_requirements = get_primary_essences(recipe)
    secondary_requierements = get_secondary_essences(recipe)
    inventory_essences = get_inventory_essences(player)
    found_primary = None
    found_secondary = None
    primary_index = 0
    old_amount = 0
    inventory = get_inventory_essences(player)
    #go through primary_requirements and inventory
    #compare the essence needed and essence in inventory
    for requirement in primary_requirements:
        for index, inventory_item in enumerate(inventory):
            if (requirement[0] == inventory_item[1] 
                and requirement[1] <= inventory_item[2]):
                found_primary = inventory_item
                #remember old essence amount and insex of primary item and subtract used essence from the inventory
                primary_index = index
                old_amount = inventory_item[2]
                
                inventory[index] = (inventory_item[0],
                                    inventory_item[1],
                                    inventory_item[2] - requirement[1]
            )

                 
                #go through secondary_requirements and inventory
                #compare the essence needed and in inventory
                for requirement in secondary_requirements:
                    for inventory_item in inventory:
                        if (requirement[0] == inventory_item[1] 
                            and requirement[1] <= inventory_item[2]):
                            #if secondary is found, return the touple
                            found_secondary = inventory_item
                        
                            return(found_primary, found_secondary)
                        
                #else drop the primary item, rest the ols amount and try the next primary.        
                if not found_secondary:

                    found_primary = None
                    inventory[index] = (inventory_item[0],
                                    inventory_item[1],
                                    old_amount)
                    

    return ()


connection = DatabaseConnection()
session = Session(connection)

recipe = session.recipes.get_by_name("Sword")

primary_requirements = get_primary_essences(recipe)
secondary_requirements = get_secondary_essences(recipe)
inventory = get_inventory_essences("Testuser")

print(primary_requirements)
print(secondary_requirements)
print(inventory)
print(crafting(recipe, "Testuser"))
