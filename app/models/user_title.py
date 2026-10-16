from sqlalchemy import BigInteger, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

from app.models.user import User
from app.models.title import Title
from app.models.watch import WatchStatus


class UserTitles(Base):
    # Represents a user's watch status for a title
    __tablename__ = "user_titles"

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

    watch_status_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("watch_statuses.id"),
        nullable=False
    )

    # Many-to-one relationship with user
    user: Mapped["User"] = relationship(
        back_populates="titles"
    )

    # Many-to-one relationship with title
    title: Mapped["Title"] = relationship(
        back_populates="user_titles"
    )

    # Many-to-one relationship with watch status
    watch_status: Mapped["WatchStatus"] = relationship(
        back_populates="user_titles"
    )

    def to_dict(self) -> dict[str, int]:
        # Convert the user title object to a dictionary
        return {
            "user_id": self.user_id,
            "title_id": self.title_id,
            "watch_status_id": self.watch_status_id
        }

    def __repr__(self) -> str:
        # Return a readable string representation of the user title
        return (
            f"UserTitles(\n"
            f"    user_id={self.user_id},\n"
            f"    title_id={self.title_id},\n"
            f"    watch_status_id={self.watch_status_id}\n"
            f")"
        )