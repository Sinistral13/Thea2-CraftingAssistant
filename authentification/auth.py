from passlib.context import CryptContext
import os
from datetime import datetime, timedelta
from jose import jwt


password_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
    )

SECRET_KEY = os.getenv("JWT_SECRET")
ALGORITHM = "HS256"


def hash_password(password):
    return password_context.hash(password)


def verify_password(password, password_hash):
    return password_context.verify(password, password_hash)


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