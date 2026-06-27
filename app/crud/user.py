from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserUpdate
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


def get_user_by_name(db: Session, user_name: str) -> User | None:
    stmt = select(User).where(User.username == user_name)
    user = db.execute(stmt).scalar_one_or_none()
    return user


def update_user(db: Session, user_id: int, update_data: UserUpdate) -> User | None:
    
    user = db.get(User, user_id)
    if user is None:
        return None
    
    update_data_dict = update_data.model_dump(exclude_unset=True)
    
    for key,value in update_data_dict.items():
        setattr(user, key, value)
    
    db.commit()
    db.refresh(user)

    return user
    

def delete_user(db: Session, user_id: int) -> User | None:
    user = db.get(User, user_id)

    if user is None:
        return None
    db.delete(user)
    db.commit()

    return user