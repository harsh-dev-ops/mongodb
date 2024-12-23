from httpx import AsyncClient
import pytest

NEW_USER_DATA = {}

def update_user_data(data: dict):
    for key, value in data.items():
        NEW_USER_DATA[key] = value


class TestUserApi:
    enpoint_url = "/users"
    create_user_data = {
            "name": "sample",
            "email": "sample@sample.com",
            "superuser": True,
            "uid": "2c856c42-2144-4df1-9c46-e3e33f432a84"
    }

    @pytest.mark.asyncio
    async def test_get_users(self, client: AsyncClient):
        response = await client.get(url = f"{self.enpoint_url}")
        assert response.status_code == 200
        assert response.json() == []

    @pytest.mark.asyncio
    async def test_create_user(self, client: AsyncClient):
        response = await client.post(url=f"{self.enpoint_url}", json=self.create_user_data)
        update_user_data(response.json())
        assert response.json()['uid'] == self.create_user_data['uid']
        assert response.status_code == 201

    @pytest.mark.asyncio
    async def test_get_user(self, client: AsyncClient):
        uid = NEW_USER_DATA['uid']
        response = await client.get(url=f"{self.enpoint_url}/{uid}")
        assert response.status_code == 200

    @pytest.mark.asyncio
    async def test_delete_user(self, client: AsyncClient):
        uid = NEW_USER_DATA['uid']
        response = await client.delete(url=f"{self.enpoint_url}/{uid}")
        assert response.status_code == 204