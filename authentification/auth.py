import bcrypt
import os
from datetime import datetime, timedelta
from jose import jwt

SECRET_KEY = os.getenv("JWT_SECRET")
ALGORITHM = "HS256"


def hash_password(password):
    password_bytes = password.encode("utf-8")

    salt = bcrypt.gensalt()

    hashed = bcrypt.hashpw(
        password_bytes,
        salt
    )

    return hashed.decode("utf-8")


def verify_password(password, password_hash):
    return bcrypt.checkpw(
        password.encode("utf-8"),
        password_hash.encode("utf-8")
    )


def create_token(username):
    payload = {
        "sub": username,
        "exp": datetime.utcnow() + timedelta(hours=24)
    }

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )


def decode_token(token):
    return jwt.decode(
        token,
        SECRET_KEY,
        algorithms=[ALGORITHM]
    )