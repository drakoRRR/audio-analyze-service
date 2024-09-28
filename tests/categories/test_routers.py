import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession


async def test_create_category(client: AsyncClient):
    category_data = {
        "title": "New Category",
        "points": ["point1", "point2"]
    }

    response = await client.post("/category/", json=category_data)

    assert response.status_code == 200
    response_data = response.json()
    assert response_data["title"] == category_data["title"]
    assert response_data["points"] == category_data["points"]


@pytest.mark.asyncio
async def test_update_category(client: AsyncClient, db_async_session: AsyncSession):
    category_data = {
        "title": "Category to Update",
        "points": ["point1"]
    }
    create_response = await client.post("/category/", json=category_data)
    category_id = create_response.json()["id"]

    updated_category_data = {
        "title": "Updated Category",
        "points": ["updated_point1", "updated_point2"]
    }
    response = await client.put(f"/category/{category_id}", json=updated_category_data)

    assert response.status_code == 200
    response_data = response.json()
    assert response_data["title"] == updated_category_data["title"]
    assert response_data["points"] == updated_category_data["points"]


@pytest.mark.asyncio
async def test_delete_category(client: AsyncClient):
    category_data = {
        "title": "Category to Delete",
        "points": ["point1", "point2"]
    }
    create_response = await client.post("/category/", json=category_data)
    category_id = create_response.json()["id"]

    delete_response = await client.delete(f"/category/{category_id}")

    assert delete_response.status_code == 200
    assert delete_response.json() == {"message": "Category deleted successfully"}


@pytest.mark.asyncio
async def test_get_all_categories(client: AsyncClient):
    category_data_1 = {
        "title": "First Category1",
        "points": ["point12"]
    }
    category_data_2 = {
        "title": "Second Category1",
        "points": ["point22"]
    }
    await client.post("/category/", json=category_data_1)
    await client.post("/category/", json=category_data_2)

    response = await client.get("/category/")

    assert response.status_code == 200
    response_data = response.json()

    assert len(response_data) >= 2
    assert response_data[0]["title"] == category_data_1["title"]
    assert response_data[1]["title"] == category_data_2["title"]
