from datetime import datetime, date
from typing import List

from sqlalchemy import Integer, String, DateTime, func, Date
from sqlalchemy.orm import relationship, Mapped, mapped_column
from database import Base


class Person(Base):
    __tablename__ = "persons"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    first_name: Mapped[str] = mapped_column(String, index=True)
    middle_name: Mapped[str] = mapped_column(String, index=True, nullable=True)
    last_name: Mapped[str] = mapped_column(String, index=True)
    contact_information: Mapped[str] = mapped_column(String)
    birth_date: Mapped[date] = mapped_column(Date)
    role: Mapped[str] = mapped_column(String)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=datetime.now, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=datetime.now, onupdate=func.now()
    )

    __mapper_args__ = {"polymorphic_on": role, "polymorphic_identity": "person"}

    def get_full_name(self):
        return f"{self.last_name} {self.first_name} {self.middle_name or ''}".strip()
