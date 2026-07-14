from dataclasses import dataclass


@dataclass
class Material:
    id: int | None
    name: str
    essence1_id: int
    amount1: float
    essence2_id: int
    amount2: float
    subtype_id: int
    composite: bool
    tier: int

    __table__ = "material"

    __columns__ = {
        "id": "id",
        "name": "name",
        
        "essence1_id": "essence1",
        "amount1": "amount1",
        "essence2_id": "essence2",
        "amount2": "amount2",
        
        "subtype_id": "subtype",
        "composite": "composite",
        "tier": "tier",
    }