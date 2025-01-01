import json
from httpx import AsyncClient
import pytest

from test.data.user_data import UserData


NEW_USER_DATA = {}


def update_user_data(data: dict):
    for key, value in data.items():
        NEW_USER_DATA[key] = value


class TestUserApi:
    enpoint_url = "/api/users"
    user_data = UserData()

    @pytest.mark.asyncio
    async def test_get_users(self, client: AsyncClient):
        response = await client.get(url=f"{self.enpoint_url}")
        assert response.status_code == 200
        assert response.json() == []

    @pytest.mark.asyncio
    async def test_create_user(self, client: AsyncClient):
        user = self.user_data.generate()
        data = user.model_dump(exclude_none=True)
        response = await client.post(url=f"{self.enpoint_url}", json=data)
        assert response.json()['uid'] == data['uid']
        assert response.status_code == 201

    @pytest.mark.asyncio
    async def test_get_user(self, client: AsyncClient):
        uid = self.user_data.user_uids[0]
        response = await client.get(url=f"{self.enpoint_url}/{uid}")
        assert response.status_code == 200

    @pytest.mark.asyncio
    async def test_delete_user(self, client: AsyncClient):
        uid = self.user_data.user_uids[0]
        response = await client.delete(url=f"{self.enpoint_url}/{uid}")
        assert response.status_code == 204
