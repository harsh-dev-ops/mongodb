from httpx import AsyncClient
import pytest

enpoint_url = "/users"

test_user_data = {
        "name": "sample",
        "email": "sample@sample.com",
        "superuser": True,
        "uid": "2c856c42-2144-4df1-9c46-e3e33f432a84"
    }

@pytest.mark.asyncio
async def test_get_users(client: AsyncClient):
    response = await client.get(url = f"{enpoint_url}")
    assert response.status_code == 200
    assert response.json() == []

@pytest.mark.asyncio
async def test_create_user(client: AsyncClient):
    response = await client.post(url=f"{enpoint_url}", json=test_user_data)
    assert response.json()['uid'] == test_user_data['uid']
    assert response.status_code == 201

@pytest.mark.asyncio
async def test_get_user(client: AsyncClient):
    uid = test_user_data['uid']
    response = await client.get(url=f"{enpoint_url}/{uid}")
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_delete_user(client: AsyncClient):
    uid = test_user_data['uid']
    response = await client.delete(url=f"{enpoint_url}/{uid}")
    assert response.status_code == 204
