
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
from app.models.season import Season


class Episode(Base):
    # Represents an episode of a season
    __tablename__ = "episodes"

    id: Mapped[int] = mapped_column(
        BigInteger,
        Identity(always=True),
        primary_key=True
    )

    season_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("seasons.id", ondelete="CASCADE"),
        nullable=False
    )

    episode_number: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    title: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    duration_minutes: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    # Many-to-one relationship with season
    season: Mapped["Season"] = relationship(
        back_populates="episodes"
    )

    __table_args__ = (
        UniqueConstraint(
            "season_id",
            "episode_number",
            name="uq_episodes_season_id_episode_number"
        ),
        CheckConstraint(
            "TRIM(title) <> ''",
            name="chk_episodes_title_not_empty"
        ),
    )

    def to_dict(self) -> dict[str, int | str | None]:
        # Converts the episode object to a dictionary
        created_at = self.created_at.isoformat() if self.created_at else None

        return {
            "id": self.id,
            "season_id": self.season_id,
            "episode_number": self.episode_number,
            "title": self.title,
            "duration_minutes": self.duration_minutes,
            "created_at": created_at
        }

    def __repr__(self) -> str:
        # Returns a readable string representation of the episode
        return (
            f"Episode(\n"
            f"    id={self.id},\n"
            f"    season_id={self.season_id},\n"
            f"    episode_number={self.episode_number},\n"
            f"    title='{self.title}',\n"
            f"    duration_minutes={self.duration_minutes},\n"
            f"    created_at={self.created_at}\n"
            f")"
        )
