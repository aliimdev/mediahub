from datetime import datetime
from typing import Optional

from sqlalchemy import DateTime, func, ForeignKey, Text, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

class UserProfile(Base):
    __tablename__="user_profiles"

    user_id: Mapped[int]=mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        primary_key=True,

        )

    full_name: Mapped[str]=mapped_column(
        String(100),
        nullable=False)

    bio:Mapped[str | None]=mapped_column(Text)

    avatar_url: Mapped(str | None)= mapped_column(Text)

    created_at: Mapped[datetime]=mapped_column(
    DateTime(timezone=True),
    server_default=func.now(),
    nullable=False
    )

    user: Mapped["User"]=relationship(
        back_populates="profiles"
    )


    def __repr__(self) -> str:
        return f"UserProfile(user_id={self.user_id}, full_name='{self.full_name}')"