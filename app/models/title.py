from datetime import datetime
from typing import Optional

from sqlalchemy import DateTime, func, ForeignKey, Text, String, BigInteger, Identity, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.models.title_type import TitleType
from app.models.season import Season
from app.models.favorite import Favorites
from app.models.review import Reviews
from app.models.user_title import UserTitles
from app.models.title_genre import TitleGenre

class Title(Base):
    __tablename__=  "titles"

    id: Mapped[int] =mapped_column(
        BigInteger,
        Identity(always=True),
        primary_key=True
        )

    title:Mapped[str]=mapped_column(
        String(255),
        nullable=False
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True)

    release_year: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True)

    title_type_id: Mapped[int] = mapped_column(
        ForeignKey("title_types.id"),
        nullable=False
    )

    duration_minutes: Mapped[int |None ] = mapped_column(
        Integer,
        nullable=True)

    created_at: Mapped[datetime] = mapped_column(
    DateTime(timezone=True),
    server_default=func.now(),
    nullable=False
    )


    # Many-to-one relationship with title type
    title_type: Mapped["TitleType"] = relationship(
        back_populates="titles"
    )

    # One-to-many relationship with title genres
    title_genres: Mapped[list["TitleGenre"]] = relationship(
        back_populates="title"
    )

    # One-to-many relationship with seasons
    seasons: Mapped[list["Season"]] = relationship(
        back_populates="title"
    )

    # One-to-many relationship with user titles
    user_titles: Mapped[list["UserTitles"]] = relationship(
        back_populates="title"
    )

    # One-to-many relationship with favorites
    favorites: Mapped[list["Favorites"]] = relationship(
        back_populates="title"
    )

    # One-to-many relationship with reviews
    reviews: Mapped[list["Reviews"]] = relationship(
        back_populates="title"
    )


    def to_dict(self) -> dict [str, int | str | None]:
        # Convert the titl object to a dictionary
        created_at: str | None = None

        if self.created_at:
            created_at = self.created_at.isoformat()

        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "release_year": self.release_year,
            "title_type_id": self.title_type_id,
            "duration_minutes": self.duration_minutes,
            "created_at": created_at
        }

    
    def __repr__(self) -> str:
        # Return a readable string representation of the title
        return (
            f"Title(\n"
            f"    id={self.id},\n"
            f"    title='{self.title}',\n"
            f"    description='{self.description}',\n"
            f"    release_year={self.release_year},\n"
            f"    title_type_id={self.title_type_id},\n"
            f"    duration_minutes={self.duration_minutes},\n"
            f"    created_at={self.created_at}\n"
            f")"
        )






    


"""
CREATE TABLE titles
(
    id BIGINT GENERATED ALWAYS AS IDENTITY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    release_year INTEGER,
    title_type_id BIGINT NOT NULL,
    duration_minutes INTEGER,
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT pk_titles_id PRIMARY KEY (id),
    CONSTRAINT fk_titles_title_type
        FOREIGN KEY (title_type_id)
        REFERENCES title_types(id)
        ON DELETE CASCADE
);"""