from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class PetDocumentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    name: str
    url: str
    created_at: datetime


class PetResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    name: str
    species: str
    gender: str
    documents: list[PetDocumentResponse]
    created_at: datetime
    updated_at: datetime
