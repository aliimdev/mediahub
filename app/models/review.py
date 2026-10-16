
from datetime import datetime

from sqlalchemy import (
    BigInteger,
    Identity,
    Numeric,
    Text,
    DateTime,
    ForeignKey,
    CheckConstraint,
    UniqueConstraint,
    func
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.models.user import User
from app.models.title import Title


class Reviews(Base):
    # Represents a user's review and rating for a title
    __tablename__ = "reviews"

    id: Mapped[int] = mapped_column(
        BigInteger,
        Identity(always=True),
        primary_key=True
    )

    user_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )

    title_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("titles.id", ondelete="CASCADE"),
        nullable=False
    )

    rating: Mapped[float] = mapped_column(
        Numeric(2, 1),
        nullable=False
    )

    comment: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    # Many-to-one relationship with user
    user: Mapped["User"] = relationship(
        back_populates="reviews"
    )

    # Many-to-one relationship with title
    title: Mapped["Title"] = relationship(
        back_populates="reviews"
    )

    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "title_id",
            name="uq_reviews_user_id_title_id"
        ),
        CheckConstraint(
            "rating BETWEEN 0 AND 10",
            name="chk_reviews_rating"
        ),
        CheckConstraint(
            "comment IS NULL OR TRIM(comment) <> ''",
            name="chk_reviews_comment_not_empty"
        ),
    )

    def to_dict(self) -> dict[str, int | float | str | None]:
        # Converts the review object to a dictionary
        created_at = self.created_at.isoformat() if self.created_at else None

        return {
            "id": self.id,
            "user_id": self.user_id,
            "title_id": self.title_id,
            "rating": float(self.rating),
            "comment": self.comment,
            "created_at": created_at
        }

    def __repr__(self) -> str:
        # Returns a readable string representation of the review
        return (
            f"Reviews(\n"
            f"    id={self.id},\n"
            f"    user_id={self.user_id},\n"
            f"    title_id={self.title_id},\n"
            f"    rating={self.rating},\n"
            f"    comment={self.comment!r},\n"
            f"    created_at={self.created_at}\n"
            f")"
        )
