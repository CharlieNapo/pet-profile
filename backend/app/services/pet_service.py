from collections.abc import Sequence
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.pet import Pet


async def get_pets(session: AsyncSession, species: str | None = None) -> Sequence[Pet]:
    stmt = select(Pet).order_by(Pet.name)
    if species is not None:
        stmt = stmt.where(Pet.species == species)
    result = await session.execute(stmt)
    return result.scalars().all()


async def get_pet_by_id(session: AsyncSession, pet_id: UUID) -> Pet | None:
    stmt = select(Pet).where(Pet.id == pet_id)
    result = await session.execute(stmt)
    return result.scalars().first()
