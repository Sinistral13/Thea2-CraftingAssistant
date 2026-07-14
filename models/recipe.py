from dataclasses import dataclass


@dataclass
class Recipe:
    id: int | None
    name: str
    primary_amount1: int
    primary_essence_id1: int
    primary_amount2: int
    primary_essence_id2: int
    primary_amount3: int
    primary_essence_id3: int
    primary_amount4: int
    primary_essence_id4: int
    secondary_amount1: int
    secondary_essence_id1: int
    secondary_amount2: int
    secondary_essence_id2: int
    secondary_amount3: int
    secondary_essence_id3: int    
    secondary_amount4: int
    secondary_essence_id4: int    

    __table__ = "recipe"

    __columns__ = {
        "id": "id",
        "name": "name",

        "primary_amount1": "primary_amount1",
        "primary_essence_id1": "primary_essence1",
        "primary_amount2": "primary_amount2",
        "primary_essence_id2": "primary_essence2",
        "primary_amount3": "primary_amount3",
        "primary_essence_id3": "primary_essence3",
        "primary_amount4": "primary_amount4",
        "primary_essence_id4": "primary_essence4",

        "secondary_amount1": "secondary_amount1",
        "secondary_essence_id1": "secondary_essence1",
        "secondary_amount2": "secondary_amount2",
        "secondary_essence_id2": "secondary_essence2",
        "secondary_amount3": "secondary_amount3",
        "secondary_essence_id3": "secondary_essence3",
        "secondary_amount4": "secondary_amount4",
        "secondary_essence_id4": "secondary_essence4"
}