from datetime import datetime
from typing import Optional


from sqlalchemy import DateTime, String, func, BigInteger, Identity
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

from app.models.user_profile import UserProfile
from app.models.user_title import UserTitles
from app.models.favorites import Favorites
from app.models.reviews import Reviews
from app.models.watch import WatchStatus


class User(Base):
    # Represents a user in the database
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        BigInteger,
        Identity(always=True),
        primary_key=True
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    # One-to-one relationship with user profile
    profiles: Mapped[Optional["UserProfile"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan",
        passive_deletes=True
    )

    # One-to-many relationship with user titles
    titles: Mapped[list["UserTitles"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan",
        passive_deletes=True
    )

    # One-to-many relationship with user favorites
    favorites: Mapped[list["Favorites"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan",
        passive_deletes=True
    )

    # One-to-many relationship with user reviews
    reviews: Mapped[list["Reviews"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan",
        passive_deletes=True
    )

    
    def to_dict(self) -> dict[str, int | str | None]:
        # Convert the user object to a dictionary
        created_at: str | None = None

        if self.created_at:
            created_at = self.created_at.isoformat()

        return {
            "id": self.id,
            "email": self.email,
            "created_at": created_at
        }



    def __repr__(self) -> str:
        # Return a readable string representation of the user
        return f"User(id={self.id}, email='{self.email}')"
