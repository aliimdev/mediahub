
from sqlalchemy import BigInteger, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.models.title import Title
from app.models.genre import Genre


class TitleGenre(Base):
    # Represents the relationship between a title and a genre
    __tablename__ = "title_genres"

    title_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("titles.id", ondelete="CASCADE"),
        primary_key=True
    )

    genre_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("genres.id", ondelete="CASCADE"),
        primary_key=True
    )

    # Many-to-one relationship with title
    title: Mapped["Title"] = relationship(
        back_populates="title_genres"
    )

    # Many-to-one relationship with genre
    genre: Mapped["Genre"] = relationship(
        back_populates="title_genres"
    )

    def to_dict(self) -> dict[str, int]:
        # Converts the title genre object to a dictionary
        return {
            "title_id": self.title_id,
            "genre_id": self.genre_id
        }

    def __repr__(self) -> str:
        # Returns a readable string representation of the title genre
        return (
            f"TitleGenre("
            f"title_id={self.title_id}, "
            f"genre_id={self.genre_id})"
        )
