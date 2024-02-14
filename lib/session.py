from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from dotenv import load_dotenv
import os

load_dotenv()
engine = create_engine(os.getenv('SQLALCHEMY_DATABASE_URL'))
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def yield_db() -> Session:
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
