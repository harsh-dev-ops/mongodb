from httpx import AsyncClient
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
import pytest_asyncio
from collections.abc import AsyncIterator
from asgi_lifespan import LifespanManager
from fastapi import FastAPI

from app.conf.settings import settings
from app.database.session import document_models
from app.main import app

async def init_db(app: FastAPI):
    app.mongo_client = AsyncIOMotorClient(settings.TEST_MONGO_URL)
    app.database = app.mongo_client.get_default_database()
    await init_beanie(app.database, document_models=document_models)

async def clear_database(app: FastAPI) -> None:
    async for collection in await app.database.list_collections():  # type: ignore[attr-defined]
        await app.database[collection["name"]].delete_many({}) 

@pytest_asyncio.fixture()
async def client() -> AsyncIterator[AsyncClient]:
    async with LifespanManager(app):
        await init_db(app)
        async with AsyncClient(app=app, base_url="http://test") as _client:
            try:
                yield _client
            except Exception as exc:
                print(exc)
            finally:
                # await clear_database(app)
                pass