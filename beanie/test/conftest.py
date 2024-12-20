from httpx import AsyncClient
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
import pytest_asyncio
import pytest
from collections.abc import AsyncIterator
from asgi_lifespan import LifespanManager
from fastapi import FastAPI

from app.conf.settings import settings
from app.database.session import document_models

settings.ENV = 'test'

from app.main import app

async def clear_database(server: FastAPI) -> None:
    async for collection in await server.database.list_collections():  # type: ignore[attr-defined]
        await server.database[collection["name"]].delete_many({}) 

@pytest_asyncio.fixture()
async def client() -> AsyncIterator[AsyncClient]:
    async with LifespanManager(app):
        async with AsyncClient(app=app, base_url="http://test") as _client:
            try:
                yield _client
            except Exception as exc:
                print(exc)
            finally:
                # await clear_database(app)
                pass