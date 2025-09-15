from passlib.context import CryptContext
import jwt
from fastapi import HTTPException, status

from datetime import datetime, timedelta

pwd_context=CryptContext(schemes=['bcrypt'], deprecated='auto')

SECRET_KEY='key'
ALGORITHM='HS256'
ACCESS_TOKEN_EXPIRE_MIN=60


def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password:str, hashed_password:str)-> bool:
    is_correct=pwd_context.verify(plain_password,hashed_password)
    return is_correct

def create_access_token(data:dict)->str:
    to_encode=data.copy()
    expire=datetime.now()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MIN)
    to_encode.update({'exp': expire})

    token=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return token

def verify_access_token(token:str)->str:
    try:
        payload=jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        return payload
    except jwt.PyJWTError:
         raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"}
        )
        
