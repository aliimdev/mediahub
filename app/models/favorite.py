
from sqlalchemy import BigInteger, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.models.user import User
from app.models.title import Title



class Favorites(Base):
    # Represents a user's favorite titles
    __tablename__ = "favorites"

    user_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("users.id", ondelete="CASCADE"),
        primary_key=True
    )

    title_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("titles.id", ondelete="CASCADE"),
        primary_key=True
    )

    # Many-to-one relationship with user
    user: Mapped["User"] = relationship(
        back_populates="favorites"
    )

    # Many-to-one relationship with title
    title: Mapped["Title"] = relationship(
        back_populates="favorites"
    )

    def to_dict(self) -> dict[str, int]:
        # Converts the favorite object to a dictionary
        return {
            "user_id": self.user_id,
            "title_id": self.title_id
        }

    def __repr__(self) -> str:
        # Returns a readable string representation of the favorite
        return (
            f"Favorites("
            f"user_id={self.user_id}, "
            f"title_id={self.title_id})"
        )
