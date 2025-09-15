from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routes import register_routes
from src.entities import *
from src.database.database import Base, engine

def create_app() -> FastAPI:
    # Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    app = FastAPI(title="FastAPI App", version="1.0.0", docs_url="/docs")
    #create all database

    origins=['http://localhost:5173']
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

    register_routes(app)

    return app

app = create_app()
