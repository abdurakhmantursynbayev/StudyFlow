from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()


DUMMY_HASH = "$argon2id$v=19$m=65536,t=3,p=4$rKABGU5wFlznMfRK14jJpA$cbI2jLwKVQBE+KbtLhgREWqUj/UsXH+BGrAwxEOVkt0"


def hash_password(password: str) -> str:
    return password_hash.hash(password)

def password_verify(plain_password: str, hashed_password: str) -> bool:
    return password_hash.verify(plain_password, hashed_password)