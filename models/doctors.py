from datetime import datetime
from typing import List

from sqlalchemy import Integer, String, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from database import Base
from models.persons import Person


class Doctor(Person):
    __tablename__ = "doctors"

    id: Mapped[int] = mapped_column(
        Integer, ForeignKey("persons.id"), primary_key=True, index=True
    )
    specialization: Mapped[str] = mapped_column(String)

    appointments: Mapped[List["Appointment"]] = relationship(
        back_populates="doctor", lazy="selectin", viewonly=True
    )

    __mapper_args__ = {"polymorphic_identity": "doctor"}

    #
    #
    # __tablename__ = 'doctors'
    #
    # id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    # model: Mapped[str] = mapped_column(String)
    # year: Mapped[int] = mapped_column(Integer)
    # registration_number: Mapped[str] = mapped_column(String, index=True)
    # capacity: Mapped[int] = mapped_column(Integer)
    #
    # medical_services: Mapped[List["MedicalService"]] = relationship(back_populates="doctor", lazy="selectin", viewonly=True)
    # appointments: Mapped[List["Appointment"]] = relationship(back_populates="doctor", lazy="selectin", viewonly=True)
    #
    # created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.now, server_default=func.now())
    # updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.now, onupdate=func.now())
