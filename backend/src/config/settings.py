import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).parent.parent.parent.parent / ".env"
if env_path.exists():
        load_dotenv(env_path)
else:
    print(".env file not found in parent folders!")


class Settings(BaseSettings):
    POSTGRES_USER:str
    POSTGRES_PASSWORD:str
    POSTGRES_DB:str
    POSTGRES_HOST:str ='localhost'
    POSTGRES_PORT: int = 5432

    @property
    def database_url(self):
        return (
            f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

settings = Settings() # type: ignore

# print("\n\n\nn\nsettings=",settings.database_url)

    