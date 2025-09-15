# service.py
from src.entities import User
from src.database.database import DbSession
from pydantic import EmailStr
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from typing import Optional

def insert_user(db: DbSession, user_data: dict) -> User:
    user = User(**user_data)
    try:
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="User with this email already exists")
    

    

def get_user_by_email(db: DbSession, user_email: EmailStr) -> Optional[User]:
    user=db.query(User).filter(User.email == user_email).first()
    return user


def update_user_profile(db, email, user_data):
    user = get_user_by_email(db, email)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    # Only update fields provided in the request
    for key, value in user_data.items():
        setattr(user, key, value)
    
    
    db.commit()
    db.refresh(user)
    return user
