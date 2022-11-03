from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from typing import Generator

from backend.core.config import settings

# PG

SQLAlCHEMY_DATABASE_URL = settings.DATABASE_URL
engine = create_engine(SQLAlCHEMY_DATABASE_URL)

# SQLITE

# SQLAlCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# engine = create_engine(SQLAlCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
