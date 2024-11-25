from typing import List
from pydantic_settings import BaseSettings
from pydantic import EmailStr, Field,  AnyHttpUrl
import os
from datetime import datetime, timezone
import pytz

asia_timezone = pytz.timezone('Asia/Kolkata')

def current_datetime() -> datetime:
    return datetime.now(asia_timezone)


class Settings(BaseSettings):
    ENV: str
    DEBUG: bool

    MONGO_INITDB_ROOT_USERNAME: str
    MONGO_INITDB_ROOT_PASSWORD: str
    MONGO_PORT: int
    MONGO_HOST: str
    MONGO_INITDB_DATABASE: str
    MONGO_DATABASE: str
    MONGO_USER: str
    MONGO_PASSWORD: str
    MONGO_URL: str = Field(
        f"""mongodb://{os.getenv('MONGO_INITDB_ROOT_USERNAME')}:{os.getenv(
        'MONGO_INITDB_ROOT_PASSWORD')}@{os.getenv('MONGO_HOST')}/{os.getenv('MONGO_INITDB_DATABASE')}?authSource=admin&retryWrites=true&w=majority""")

    CLIENT_ORIGIN: str
    ALLOWED_ORIGIN: List[str] = os.getenv('CLIENT_ORIGIN', "http://localhost:3000").split(",")
    APP_URL: str

    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_DB: int

    REDIS_BROKER_URL: str = Field(
        os.getenv('REDIS_BROKER_URL',"redis://localhost:6379/0"))
    REDIS_BACKEND_URL: str = Field(
        os.getenv('REDIS_BACKEND_URL', "redis://localhost:6379/0"))

    class config:
        env_file = '.env'


settings = Settings()
