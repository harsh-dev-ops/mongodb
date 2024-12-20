from httpx import AsyncClient
import pytest

enpoint_url = "/users"

@pytest.mark.asyncio
async def test_get_users(client: AsyncClient):
    response = await client.get(url = f"{enpoint_url}")
    assert response.status_code == 200