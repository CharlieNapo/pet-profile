import uuid
from datetime import datetime, timezone

from sqlalchemy import CheckConstraint, DateTime, ForeignKey, String, Text, Uuid, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


def _utcnow() -> datetime:
    return datetime.now(timezone.utc).replace(tzinfo=None)


class Pet(Base):
    __tablename__ = "pets"
    __table_args__ = (
        CheckConstraint("species IN ('cat', 'dog')", name="ck_pets_species"),
        CheckConstraint("gender IN ('male', 'female')", name="ck_pets_gender"),
    )

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid, primary_key=True, default=uuid.uuid4, server_default=text("gen_random_uuid()")
    )
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    species: Mapped[str] = mapped_column(String(10), nullable=False)
    gender: Mapped[str] = mapped_column(String(10), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, default=_utcnow, server_default=text("now()")
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, default=_utcnow, server_default=text("now()"), onupdate=_utcnow
    )

    documents: Mapped[list["PetDocument"]] = relationship(
        "PetDocument", back_populates="pet", lazy="selectin", cascade="all, delete-orphan"
    )


class PetDocument(Base):
    __tablename__ = "pet_documents"

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid, primary_key=True, default=uuid.uuid4, server_default=text("gen_random_uuid()")
    )
    pet_id: Mapped[uuid.UUID] = mapped_column(
        Uuid, ForeignKey("pets.id", ondelete="CASCADE"), nullable=False, index=True
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    url: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, default=_utcnow, server_default=text("now()")
    )

    pet: Mapped["Pet"] = relationship("Pet", back_populates="documents")
