import uuid

from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from tests.conftest import make_document, make_pet


async def test_list_pets_empty(client: AsyncClient):
    response = await client.get("/api/pets")
    assert response.status_code == 200
    assert response.json() == []


async def test_list_pets(client: AsyncClient, db_session: AsyncSession):
    db_session.add_all([make_pet(name="Bella"), make_pet(name="Max")])
    await db_session.commit()

    response = await client.get("/api/pets")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    names = {p["name"] for p in data}
    assert names == {"Bella", "Max"}


async def test_list_pets_filter_species(client: AsyncClient, db_session: AsyncSession):
    db_session.add(make_pet(name="Rex", species="dog"))
    db_session.add(make_pet(name="Whiskers", species="cat"))
    await db_session.commit()

    response = await client.get("/api/pets?species=dog")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["name"] == "Rex"


async def test_list_pets_invalid_species(client: AsyncClient):
    response = await client.get("/api/pets?species=bird")
    assert response.status_code == 422


async def test_get_pet_by_id(client: AsyncClient, db_session: AsyncSession):
    pet = make_pet(name="Bella", species="dog", gender="female")
    db_session.add(pet)
    await db_session.commit()

    response = await client.get(f"/api/pets/{pet.id}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Bella"
    assert data["species"] == "dog"
    assert data["gender"] == "female"
    assert "documents" in data
    assert "id" in data


async def test_get_pet_not_found(client: AsyncClient):
    response = await client.get(f"/api/pets/{uuid.uuid4()}")
    assert response.status_code == 404
    assert response.json()["detail"] == "Pet not found"


async def test_get_pet_invalid_id(client: AsyncClient):
    response = await client.get("/api/pets/not-a-uuid")
    assert response.status_code == 422


async def test_pet_response_includes_documents(client: AsyncClient, db_session: AsyncSession):
    pet = make_pet(name="Max")
    doc = make_document(name="Vaccination Record", url="https://example.com/vacc.pdf")
    pet.documents = [doc]
    db_session.add(pet)
    await db_session.commit()

    response = await client.get(f"/api/pets/{pet.id}")
    assert response.status_code == 200
    data = response.json()
    assert len(data["documents"]) == 1
    assert data["documents"][0]["name"] == "Vaccination Record"
    assert data["documents"][0]["url"] == "https://example.com/vacc.pdf"
    assert "id" in data["documents"][0]
