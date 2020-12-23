from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def is_valid(password: str, hashed_password: str) -> bool:
    return pwd_context.verify(password, hashed_password)