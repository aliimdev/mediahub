
from sqlalchemy import BigInteger, Identity, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.models.title import Title


class TitleType(Base):
    # Represents a title type in the database
    __tablename__ = "title_types"

    id: Mapped[int] = mapped_column(
        BigInteger,
        Identity(always=True),
        primary_key=True
    )

    type: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        unique=True
    )

    # One-to-many relationship with titles
    titles: Mapped[list["Title"]] = relationship(
        back_populates="title_type"
    )

    def to_dict(self) -> dict[str, int | str]:
        # Converts the title type object to a dictionary
        return {
            "id": self.id,
            "type": self.type
        }

    def __repr__(self) -> str:
        # Returns a readable string representation of the title type
        return f"TitleType(id={self.id}, type='{self.type}')"
