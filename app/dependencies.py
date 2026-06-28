from app.core.database import SessionFactory
from collections.abc import Generator
from sqlalchemy.orm import Session

def get_db() -> Generator[Session, None, None]:
    db = SessionFactory()

    try:
        yield db
    finally:
        db.close()