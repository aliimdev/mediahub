from datetime import datetime
from typing import Optional

from sqlalchemy import DateTime, String, func, BigInteger, Identity
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

class User(Base):
    __tablename__="users"


    id: Mapped[int]=mapped_column(
        BigInteger, 
        Identity(always=True),
        primary_key=True
        )
    
    email: Mapped[str]=mapped_column(
        String(255),
        unique=True,
        nullable=False
    )

    created_at: Mapped[datetime]=mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )



    profiles: Mapped[Optional["UserProfile"]]=relationship(
        back_populates="user",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )

    titles: Mapped[list["UserTitles"]]=relationship(
        back_populates="user",
        cascade="all, delete-orphan",
        passive_deletes=True
    )

    favorites: Mapped[list["Favorites"]]=relationship(
        back_populates="user",
        cascade="all, delete-orphan",
        passive_deletes=True
    )

    reviews: Mapped[list["Reviews"]]=relationship(
        back_populates="user",
        cascade="all, delete-orphan",
        passive_deletes=True       
    )
    def __repr__(self) -> str:
        return f"User(id={self.id}, email='{self.email}')"
