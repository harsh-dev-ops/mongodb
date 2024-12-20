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


async def clear_database(app: FastAPI) -> None:
    async for collection in await app.database.list_collections():  # type: ignore[attr-defined]
        print(collection)
        await app.database[collection["name"]].delete_many({}) 

@pytest_asyncio.fixture()
async def client() -> AsyncIterator[AsyncClient]:
    async with LifespanManager(app):
        async with AsyncClient(app) as _client:
            try:
                app.client = AsyncIOMotorClient(settings.TEST_MONGO_URL)
                app.database = app.client.get_default_database()
                await init_beanie(app.database, document_models=document_models)
                yield _client
            except Exception as exc:
                print(exc)
            finally:
                await clear_database(app)