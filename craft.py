from repository import RecipeRepository, MaterialRepository, InventoryRepository


def extract_primary(recipe):
    """
    Returns:
    {
        essence_id: amount
    }
    """
    return extract_requirements([
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
    ])
    

def extract_secondary(recipe):
    """
    Returns:
    {
        essence_id: amount
    }
    """
    return extract_requirements([
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
    ])


def get_essences_in_inventory(required_essence, inventory):
    """
    Takes required essence as a touple(essence_id, amount).
    Checks the inventory for materials with that essence.
    If found, compares the required and availible amount
    ()

    """
    for material in inventory:
        essence1 = MaterialRepository.get_by_id(
            material.essence1
        )
        
        if essence1 != required_essence[0] and material.essence2:
            if essence2 == required_essence:
                return
                

        




def craft(recipe, player):
    """
    Returns True if the player has enough materials/essence
    to craft the recipe.
    """
    #get possible essences
    primary = extract_primary(recipe)
    secondary = extract_secondary(recipe)

    #get player inventory
    inventory = InventoryRepository.get_by_player(player)

    # Check primary requirements
    if not check_essences(primary, inventory):
        return False

    # Check secondary requirements
    if not check_essences(secondary, inventory):
        return False

    return True