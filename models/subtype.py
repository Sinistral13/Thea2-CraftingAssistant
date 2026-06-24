from dataclasses import dataclass


@dataclass
class Subtype:
    id: int | None
    name: str