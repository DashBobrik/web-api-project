from datetime import datetime
from typing import List

from sqlalchemy import Integer, String, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from database import Base
from models.persons import Person


class Patient(Person):
    __tablename__ = "patients"

    id: Mapped[int] = mapped_column(
        Integer, ForeignKey("persons.id"), primary_key=True, index=True
    )
    insurance_number: Mapped[str] = mapped_column(String, index=True, unique=True)

    appointments: Mapped[List["Appointment"]] = relationship(
        back_populates="patient", lazy="selectin", viewonly=True
    )

    __mapper_args__ = {"polymorphic_identity": "patient"}


# class Patient(Base):
#     __tablename__ = 'patients'
#
#     id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
#     first_name: Mapped[str] = mapped_column(String, index=True)
#     middle_name: Mapped[str] = mapped_column(String, index=True, nullable=True)
#     last_name: Mapped[str] = mapped_column(String, index=True)
#     contact_information: Mapped[str] = mapped_column(String)
#
#     appointments: Mapped[List["Appointment"]] = relationship(back_populates="patient", lazy="selectin", viewonly=True)
#
#     created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.now, server_default=func.now())
#     updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.now, onupdate=func.now())
#
#     def get_full_name(self):
#         return f"{self.last_name} {self.first_name} {self.middle_name}".sappointment()
