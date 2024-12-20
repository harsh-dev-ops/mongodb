from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from contextlib import asynccontextmanager
from logging import info

from app.api.views.users.models import UserModel
from app.conf.settings import settings


document_models = [
    UserModel
    ]

MONGO_URI = settings.TEST_MONGO_URL if settings.ENV == 'test' else settings.MONGO_URL

@asynccontextmanager
async def db_lifespan(app: FastAPI):
    # Startup
    # breakpoint()
    app.mongo_client = AsyncIOMotorClient(settings.MONGO_URL)
    app.database = app.mongo_client.get_default_database()
    await init_beanie(app.database, document_models=document_models)
    ping_response = await app.database.command("ping")
    if int(ping_response["ok"]) != 1:
        raise Exception("Problem connecting to database cluster.")
    else:
        info("Connected to database cluster.")
    yield

    # Shutdown
    app.mongo_client.close()
