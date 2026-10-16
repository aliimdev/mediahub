
from datetime import datetime

from sqlalchemy import (
    BigInteger,
    Identity,
    Integer,
    String,
    DateTime,
    ForeignKey,
    CheckConstraint,
    UniqueConstraint,
    func
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.models.title import Title
from app.models.episode import Episode


class Season(Base):
    # Represents a season of a series
    __tablename__ = "seasons"

    id: Mapped[int] = mapped_column(
        BigInteger,
        Identity(always=True),
        primary_key=True
    )

    title_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("titles.id", ondelete="CASCADE"),
        nullable=False
    )

    season_number: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    title: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    # Many-to-one relationship with title
    title_obj: Mapped["Title"] = relationship(
        back_populates="seasons"
    )

    # One-to-many relationship with episodes
    episodes: Mapped[list["Episode"]] = relationship(
        back_populates="season",
        cascade="all, delete-orphan",
        passive_deletes=True
    )

    __table_args__ = (
        UniqueConstraint(
            "title_id",
            "season_number",
            name="uq_seasons_title_id_season_number"
        ),
        CheckConstraint(
            "season_number > 0",
            name="chk_seasons_season_number"
        ),
        CheckConstraint(
            "TRIM(title) <> ''",
            name="chk_seasons_title_not_empty"
        ),
    )

    def to_dict(self) -> dict[str, int | str | None]:
        # Converts the season object to a dictionary
        created_at = self.created_at.isoformat() if self.created_at else None

        return {
            "id": self.id,
            "title_id": self.title_id,
            "season_number": self.season_number,
            "title": self.title,
            "created_at": created_at
        }

    def __repr__(self) -> str:
        # Returns a readable string representation of the season
        return (
            f"Season(\n"
            f"    id={self.id},\n"
            f"    title_id={self.title_id},\n"
            f"    season_number={self.season_number},\n"
            f"    title='{self.title}',\n"
            f"    created_at={self.created_at}\n"
            f")"
        )
