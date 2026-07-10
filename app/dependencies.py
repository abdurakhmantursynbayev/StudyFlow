from app.core.database import SessionFactory
from collections.abc import Generator
from sqlalchemy.orm import Session
import jwt
from jwt.exceptions import InvalidTokenError
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from app.core.config import SECRET_KEY, ALGORITHM
from app.schemas.token import AccessTokenData
from app.crud.user import get_user_by_id
from app.models.user import User


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_db() -> Generator[Session, None, None]:
    db = SessionFactory()

    try:
        yield db
    finally:
        db.close()
    

def get_current_user(
        active_token: Annotated[str, Depends(oauth2_scheme)],
        db: Annotated[Session, Depends(get_db)]
    ) -> User:

    credential_exceptions = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )


    try:
        payload = jwt.decode(active_token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        if user_id is None:
            raise credential_exceptions
        token_data = AccessTokenData(user_id=int(user_id))
    except InvalidTokenError:
        raise credential_exceptions
    
    user = get_user_by_id(db, token_data.user_id)
    if user is None:
        raise credential_exceptions
    return user

