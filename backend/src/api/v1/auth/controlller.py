from fastapi import APIRouter, HTTPException
from src.api.v1.auth.model import *
from src.database.database import DbSession
from src.api.v1.auth.service import *
from src.api.v1.auth.utils import *
from pydantic import EmailStr
from src.entities import *

auth_router=APIRouter()



@auth_router.get("/health")
async def v1_health():
    return {"message":"API version 1 (v1) is healthy"}


@auth_router.post("/register")
async def register_user(user_data: AuthUser, db: DbSession):
    existing_user=get_user_by_email(db, user_data.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email is already registered")
    
    hashed_password=hash_password(user_data.password)
    new_user_data = {
        "email": user_data.email,
        "password_hash": hashed_password,
       
    }

    newuser=insert_user(db, new_user_data)

    return {
        "message":"user registered successfully",
        "user_email":newuser.email
    }

@auth_router.post("/login", response_model=TokenResponse)
async def login_user(user_data: AuthUser, db: DbSession):
    user = get_user_by_email(db, user_data.email)
    
    if user is None or not verify_password(user_data.password, user.password_hash): # type: ignore
        raise HTTPException(status_code=401, detail="Invalid Credentials")
    
    access_token = create_access_token(data={"sub": user.email})
    
    return TokenResponse(
        message="Logged in successfully",
        access_token=access_token,
        token_type="bearer"
    )


@auth_router.put("/update_profile")
async def update_profile(user_data: UserData, db: DbSession):
    update_data = user_data.dict(exclude_unset=True)
    updated_user = update_user_profile(db, user_data.email, update_data)


    return {
        "message": "User profile updated successfully",
        "user_email": updated_user.email
    }

@auth_router.get("/user/{user_email}", response_model=UserRead)
async def get_user_detail(user_email:EmailStr, db: DbSession):
    user=get_user_by_email(db, user_email)
    if not user:
        raise HTTPException(status_code=404 , detail="User not found")
    return user


