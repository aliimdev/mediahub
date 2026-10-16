
from sqlalchemy import BigInteger, Identity, String, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base



class WatchStatus(Base):
    # Represents a watch status in the database
    __tablename__ = "watch_statuses"

    id: Mapped[int] = mapped_column(
        BigInteger,
        Identity(always=True),
        primary_key=True
    )

    status: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        unique=True
    )

    # One-to-many relationship with user titles
    user_titles: Mapped[list["UserTitles"]] = relationship(
        back_populates="watch_status"
    )

    __table_args__ = (
        CheckConstraint(
            "TRIM(status) <> ''",
            name="chk_watch_statuses_status_not_empty"
        ),
    )

    def to_dict(self) -> dict[str, int | str]:
        # Converts the watch status object to a dictionary
        return {
            "id": self.id,
            "status": self.status
        }

    def __repr__(self) -> str:
        # Returns a readable string representation of the watch status
        return f"WatchStatus(id={self.id}, status='{self.status}')"
