from sqlalchemy import create_engine
from app.core.config import DATABASE_URL
from sqlalchemy.orm import sessionmaker

engine = create_engine(DATABASE_URL)

SessionFactory = sessionmaker(
    bind=engine,
    expire_on_commit=False
)