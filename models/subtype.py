from dataclasses import dataclass

@dataclass
class Subtype:
    id: int | None
    name: str

    __table__ = "subtype"

    __columns__ = {
        "id": "id",
        "name": "name"
    }