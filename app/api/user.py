from fastapi import APIRouter, Depends
from app.dependencies import get_db
from typing import Annotated
from sqlalchemy.orm import Session
from app.schemas.user import UserRead, UserUpdate
from app.crud.user import get_user_by_id, get_user_by_name, update_user, delete_user



router = APIRouter(
    prefix="/me",
    tags=["USER"]
)

@router.get("/{user_id}", response_model=UserRead)
def get_user(user_id: int, db: Annotated[Session, Depends(get_db)]):
    return get_user_by_id(db, id)


@router.patch("/{user_id}", response_model=UserRead)
def update_user_(user_id: int, user_new_data: UserUpdate, db: Annotated[Session, Depends(get_db)]):
    updated_user = update_user(db, user_id, user_new_data)
    return updated_user


@router.delete("/{user_id}", response_model=UserRead)
def delete_user_(
    user_id: int,
    db: Annotated[Session, Depends(get_db)]
):
    return delete_user(db, user_id)
