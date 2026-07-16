from dataclasses import dataclass

@dataclass
class AppUser:
    username: str
    password: str

    __table__ = "usertable"

    __columns__ = {
        "name": "username",
        "password": "password"
    }