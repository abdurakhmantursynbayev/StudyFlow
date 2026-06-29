from fastapi import APIRouter, Depends
from app.schemas.user import UserCreate, UserRead
from app.crud.user import create_user
from app.dependencies import get_db
from typing import Annotated
from sqlalchemy.orm import Session

router = APIRouter(prefix="/auth", tags=["AUTH"])

@router.post("/register", response_model=UserRead, status_code=201)
def register_user(user_data: UserCreate, db: Annotated[Session, Depends(get_db)]):
    new_user = create_user(db, user_data)
    return new_user


