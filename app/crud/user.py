from sqlalchemy.orm import Session
from app.schemas.user import UserCreate
from app.models.user import User
from app.core.security import hash_password
from sqlalchemy import select


def create_user(db: Session, user: UserCreate) -> User:
    hashed_password = hash_password(password=user.password)

    new_user = User(
        username = user.username,
        full_name = user.full_name,
        hashed_password = hashed_password,
        role = user.role
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def get_user_by_id(db: Session, user_id: int) -> User | None:
    return db.get(User, user_id)




    