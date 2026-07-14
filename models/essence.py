from dataclasses import dataclass

@dataclass
class Essence:
    id: int | None
    name: str

    __table__ = "essence"

    __columns__ = {
        "id": "id",
        "name": "name"
    }