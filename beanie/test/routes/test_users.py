from httpx import AsyncClient
import pytest



sample_user_data = {
        "name": "sample",
        "email": "sample@sample.com",
        "superuser": True,
        "uid": "2c856c42-2144-4df1-9c46-e3e33f432a84"
}


class TestUserApi:
    enpoint_url = "/users"
    
    # @pytest.mark.asyncio
    async def test_get_users(self, client: AsyncClient):
        response = await client.get(url = f"{self.enpoint_url}")
        assert response.status_code == 200
        assert response.json() == []

    # @pytest.mark.asyncio
    async def test_create_user(self, client: AsyncClient):
        response = await client.post(url=f"{self.enpoint_url}", json=sample_user_data)
        assert response.json()['uid'] == sample_user_data['uid']
        assert response.status_code == 201

    # @pytest.mark.asyncio
    async def test_get_user(self, client: AsyncClient):
        uid = sample_user_data['uid']
        response = await client.get(url=f"{self.enpoint_url}/{uid}")
        assert response.status_code == 200

    # @pytest.mark.asyncio
    async def test_delete_user(self, client: AsyncClient):
        uid = sample_user_data['uid']
        response = await client.delete(url=f"{self.enpoint_url}/{uid}")
        assert response.status_code == 204
