from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.schemas.pet import PetResponse
from app.services.pet_service import get_pet_by_id, get_pets

router = APIRouter(prefix="/api/pets", tags=["pets"])


@router.get("", response_model=list[PetResponse])
async def list_pets(
    species: str | None = Query(None, pattern="^(cat|dog)$"),
    session: AsyncSession = Depends(get_db),
) -> list[PetResponse]:
    pets = await get_pets(session, species=species)
    return [PetResponse.model_validate(p) for p in pets]


@router.get("/{pet_id}", response_model=PetResponse)
async def get_pet(
    pet_id: UUID,
    session: AsyncSession = Depends(get_db),
) -> PetResponse:
    pet = await get_pet_by_id(session, pet_id)
    if pet is None:
        raise HTTPException(status_code=404, detail="Pet not found")
    return PetResponse.model_validate(pet)
