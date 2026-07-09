from sqlalchemy.orm import Session
from app.crud.user import get_user_by_name
from app.core.security import password_verify, DUMMY_HASH
from app.models.user import User


def authenticate_user(db: Session, username: str, password: str) -> User | bool:
    user = get_user_by_name(db, username)
    if user is None: 
        password_verify(password, DUMMY_HASH)
        return False
    if not password_verify(password, user.hashed_password):
        return False
    return user

