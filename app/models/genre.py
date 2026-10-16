
from sqlalchemy import BigInteger, Identity, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.models.title_genres import TitleGenres


class Genre(Base):
    # Represents a genre in the database
    __tablename__ = "genres"

    id: Mapped[int] = mapped_column(
        BigInteger,
        Identity(always=True),
        primary_key=True
    )

    name: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        unique=True
    )

    # One-to-many relationship with title genres
    title_genres: Mapped[list["TitleGenres"]] = relationship(
        back_populates="genre"
    )

    def to_dict(self) -> dict[str, int | str]:
        # Converts the genre object to a dictionary
        return {
            "id": self.id,
            "name": self.name
        }

    def __repr__(self) -> str:
        # Returns a readable string representation of the genre
        return f"Genre(id={self.id}, name='{self.name}')"
