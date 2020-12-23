from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from ..models.user import User
from ..models import password_verifier
from ..repositories import user_repository

router = APIRouter()

def is_authenticated(username: str, password: str) -> bool:
    user = user_repository.get_user(username)
    if user == None:
        return False
    if not password_verifier.is_valid(password, user.password):
        return False
    return True

@router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    username = form_data.username
    password = form_data.password
    if not is_authenticated(username, password):
        raise HTTPException(status_code=400, detail="Incorrect username or password.")
    return { "access_token": username, "token_type": "bearer" }