from typing import List
from pydantic_settings import BaseSettings
from pydantic import EmailStr, Field,  AnyHttpUrl
import os
from datetime import datetime, timezone
import pytz

asia_timezone = pytz.timezone('Asia/Kolkata')

def current_datetime() -> datetime:
    return datetime.now(asia_timezone)

def _mongo_url():
    root_user_name = os.getenv('MONGO_INITDB_ROOT_USERNAME')
    root_password = os.getenv('MONGO_INITDB_ROOT_PASSWORD')
    host = os.getenv('MONGO_HOST')
    port = os.getenv('MONGO_PORT')
    init_database = os.getenv('MONGO_DATABASE')
    url = f"mongodb://{root_user_name}:{root_password}@{host}:{port}/{init_database}?authSource=admin&retryWrites=true&w=majority"
    return url


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
    MONGO_URL: str = Field(_mongo_url())

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
