from fastapi import APIRouter, Depends
from app.dependencies import get_db, get_current_user
from typing import Annotated
from sqlalchemy.orm import Session
from app.schemas.user import UserRead, UserUpdate
from app.crud.user import update_user, delete_user
from app.models.user import User



router = APIRouter(
    prefix="/me",
    tags=["USER"]
)

@router.get("/", response_model=UserRead)
def read_me(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user


@router.patch("/{user_id}", response_model=UserRead)
def update_current_user(user_id: int, user_new_data: UserUpdate, db: Annotated[Session, Depends(get_db)]):
    updated_user = update_user(db, user_id, user_new_data)
    return updated_user


@router.delete("/{user_id}", response_model=UserRead)
def delete_current_user(
    user_id: int,
    db: Annotated[Session, Depends(get_db)]
):
    return delete_user(db, user_id)
