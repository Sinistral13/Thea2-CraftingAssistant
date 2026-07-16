from dataclasses import dataclass


@dataclass
class Inventory:
    id: int | None
    player: str
    material: int
    amount: int

    __table__ = "inventory"

    __columns__ = {
        "id": "id",
        "player": "player",
        "material": "material",
        "amount": "amount",
    }