from sqlalchemy import create_engine #connects python with postgreSQL
from sqlalchemy.ext.declarative import declarative_base #will be used in Base model so that we can define table schema like python class
from sqlalchemy.orm import sessionmaker, Session # for creating database sessions
from src.config.settings import settings
from typing import Annotated
from fastapi import Depends

DATABASE_URL=settings.database_url

# DATABASE_URL="postgresql+psycopg2://admin:admin123@postgres-db:5432/database"
# Engine → connects SQLAlchemy to PostgreSQL
engine=create_engine(DATABASE_URL)

# Session → used to talk to DB
SessionLocal=sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base=declarative_base()


def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close() 


DbSession = Annotated[Session, Depends(get_db)] #for safter type check when DbSession is called
        