from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.user import UserCreate, UserRead
from app.crud.user import create_user
from app.dependencies import get_db
from typing import Annotated
from sqlalchemy.orm import Session
from app.core.auth import authenticate_user
from fastapi.security import OAuth2PasswordRequestForm
from app.core.security import create_access_token
from app.core.config import ACCESS_TOKEN_EXPIRE_MINUTES
from datetime import timedelta
from app.schemas.token import Token

router = APIRouter(prefix="/auth", tags=["AUTH"])

@router.post("/register", response_model=UserRead, status_code=201)
def register_user(user_data: UserCreate, db: Annotated[Session, Depends(get_db)]):
    new_user = create_user(db, user_data)
    return new_user


@router.post("/login")
def login_for_access_token(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
        db: Annotated[Session, Depends(get_db)]
    ):

    user = authenticate_user(
        db,
        form_data.username,
        form_data.password
    )

    if not user: 
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"}
        )
    payload = {
        "sub": str(user.id)
    }
    exp_minutes = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token = create_access_token(payload=payload, expiration=exp_minutes)
    return Token(access_token=token, token_type="bearer")