from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from contextlib import asynccontextmanager
from logging import info

from app.api.views.users.models import User
from app.conf.settings import settings


@asynccontextmanager
async def db_lifespan(app: FastAPI):
    # Startup
    # breakpoint()
    app.client = AsyncIOMotorClient(settings.MONGO_URL)
    app.database = app.client.get_default_database()
    await init_beanie(app.database, document_models=[
        User
    ])
    ping_response = await app.database.command("ping")
    if int(ping_response["ok"]) != 1:
        raise Exception("Problem connecting to database cluster.")
    else:
        info("Connected to database cluster.")
    yield

    # Shutdown
    app.client.close()
