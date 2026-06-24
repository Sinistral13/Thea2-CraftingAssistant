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