from sqlalchemy.ext.asyncio import AsyncSession

from app.services.pet_service import get_pet_by_id, get_pets
from tests.conftest import make_document, make_pet


async def test_get_pets_empty(db_session: AsyncSession):
    result = await get_pets(db_session)
    assert result == []


async def test_get_pets_returns_all(db_session: AsyncSession):
    pets = [make_pet(name=n) for n in ["Alpha", "Beta", "Gamma"]]
    db_session.add_all(pets)
    await db_session.commit()

    result = await get_pets(db_session)
    assert len(result) == 3


async def test_get_pets_ordered_by_name(db_session: AsyncSession):
    for name in ["Charlie", "Alpha", "Bravo"]:
        db_session.add(make_pet(name=name))
    await db_session.commit()

    result = await get_pets(db_session)
    names = [p.name for p in result]
    assert names == ["Alpha", "Bravo", "Charlie"]


async def test_get_pets_filter_by_species(db_session: AsyncSession):
    db_session.add(make_pet(name="Rex", species="dog"))
    db_session.add(make_pet(name="Whiskers", species="cat"))
    await db_session.commit()

    dogs = await get_pets(db_session, species="dog")
    assert len(dogs) == 1
    assert dogs[0].name == "Rex"

    cats = await get_pets(db_session, species="cat")
    assert len(cats) == 1
    assert cats[0].name == "Whiskers"


async def test_get_pets_filter_no_match(db_session: AsyncSession):
    db_session.add(make_pet(name="Rex", species="dog"))
    await db_session.commit()

    result = await get_pets(db_session, species="cat")
    assert result == []


async def test_get_pet_by_id_found(db_session: AsyncSession):
    pet = make_pet(name="Bella", species="dog", gender="female")
    db_session.add(pet)
    await db_session.commit()

    result = await get_pet_by_id(db_session, pet.id)
    assert result is not None
    assert result.name == "Bella"
    assert result.species == "dog"
    assert result.gender == "female"


async def test_get_pet_by_id_not_found(db_session: AsyncSession):
    import uuid

    result = await get_pet_by_id(db_session, uuid.uuid4())
    assert result is None


async def test_get_pet_includes_documents(db_session: AsyncSession):
    pet = make_pet(name="Max")
    doc = make_document(name="Vaccination Record", url="https://example.com/vacc.pdf")
    pet.documents = [doc]
    db_session.add(pet)
    await db_session.commit()

    result = await get_pet_by_id(db_session, pet.id)
    assert result is not None
    assert len(result.documents) == 1
    assert result.documents[0].name == "Vaccination Record"
