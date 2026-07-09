from pwdlib import PasswordHash
from datetime import datetime, timedelta, timezone
import jwt
from app.core.config import SECRET_KEY
from app.core.config import ALGORITHM

password_hash = PasswordHash.recommended()


DUMMY_HASH = "$argon2id$v=19$m=65536,t=3,p=4$rKABGU5wFlznMfRK14jJpA$cbI2jLwKVQBE+KbtLhgREWqUj/UsXH+BGrAwxEOVkt0"


def hash_password(password: str) -> str:
    return password_hash.hash(password)

def password_verify(plain_password: str, hashed_password: str) -> bool:
    return password_hash.verify(plain_password, hashed_password)

def create_access_token(payload: dict, expiration: timedelta | None = None):
    payload_data = payload.copy()
    if expiration:
        expiration_time = datetime.now(timezone.utc) + expiration
    else:
        expiration_time = datetime.now(timezone.utc) + timedelta(minutes=15)
    payload_data.update({"exp": expiration_time})
    encode_jwt = jwt.encode(payload_data, SECRET_KEY, algorithm=[ALGORITHM])
    return encode_jwt



