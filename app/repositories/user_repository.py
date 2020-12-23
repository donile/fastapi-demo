from typing import Dict
from ..models.user import User
from ..models import password_verifier

users_db: Dict[str, User] = {
    "mdonile": User(**{
        "username": "mdonile",
        "password": password_verifier.pwd_context.hash("password")
    })
}

def get_user(id: str) -> User:
    return users_db[id]