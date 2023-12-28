from datetime import datetime
from typing import List

from sqlalchemy import Integer, DateTime, func, ForeignKey, Date, String, Float
from sqlalchemy.orm import relationship, Mapped, mapped_column
from database import Base


class MedicalService(Base):
    __tablename__ = "medical_services"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    cost: Mapped[float] = mapped_column(Float)

    appointments: Mapped[List["Appointment"]] = relationship(
        back_populates="medical_service", lazy="selectin", viewonly=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=datetime.now, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=datetime.now, onupdate=func.now()
    )


#
# class MedicalService(Base):
#     __tablename__ = 'medical_services'
#
#     id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
#     start_point: Mapped[str] = mapped_column(String)
#     end_point: Mapped[str] = mapped_column(String)
#     duration: Mapped[str] = mapped_column(String)
#
#     doctor_id: Mapped[int] = mapped_column(Integer, ForeignKey('doctors.id'), nullable=True)
#     doctor: Mapped["Doctor"] = relationship(back_populates="medical_services", lazy="selectin", viewonly=True)
#
#     appointments: Mapped[List["Appointment"]] = relationship(back_populates="medical_service", lazy="selectin", viewonly=True)
#
#     created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.now, server_default=func.now())
#     updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.now, onupdate=func.now())
