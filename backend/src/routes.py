from fastapi import FastAPI
from src.api.v1 import api_v1_router


def register_routes(app: FastAPI):
    #register all the routes here for each versions
    app.include_router(api_v1_router,prefix="/api/v1")


    