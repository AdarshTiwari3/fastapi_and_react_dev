from fastapi import APIRouter
from src.api.v1.auth.controlller import auth_router


api_v1_router=APIRouter()

#register the api endpoints route here

api_v1_router.include_router(auth_router,prefix="/auth",tags=["Auth v1"])