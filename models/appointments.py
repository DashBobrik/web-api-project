from datetime import datetime

from sqlalchemy import Integer, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from database import Base


class Appointment(Base):
    __tablename__ = "appointments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    appointment_time: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    doctor_id: Mapped[int] = mapped_column(Integer, ForeignKey("doctors.id"))
    patient_id: Mapped[int] = mapped_column(Integer, ForeignKey("patients.id"))
    medical_service_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("medical_services.id")
    )

    doctor: Mapped["Doctor"] = relationship(
        back_populates="appointments", lazy="selectin", viewonly=True
    )
    patient: Mapped["Patient"] = relationship(
        back_populates="appointments", lazy="selectin", viewonly=True
    )
    medical_service: Mapped["MedicalService"] = relationship(
        back_populates="appointments", lazy="selectin", viewonly=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=datetime.now, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=datetime.now, onupdate=func.now()
    )


# class Appointment(Base):
#     __tablename__ = 'appointments'
#
#     id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
#     start_time = mapped_column(DateTime(timezone=True), server_default=func.now())
#     doctor_id: Mapped[int] = mapped_column(Integer, ForeignKey('doctors.id'), nullable=True)
#     patient_id: Mapped[int] = mapped_column(Integer, ForeignKey('patients.id'), nullable=True)
#     medical_service_id = mapped_column(Integer, ForeignKey('medical_services.id'))
#
#     doctor: Mapped["Doctor"] = relationship(back_populates="appointments", lazy="selectin", viewonly=True)
#     patient: Mapped["Patient"] = relationship(back_populates="appointments", lazy="selectin", viewonly=True)
#     medical_service: Mapped["MedicalService"] = relationship(back_populates="appointments", lazy="selectin", viewonly=True)
#
#     created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.now,
#                                                  server_default=func.now())
#     updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.now, onupdate=func.now())
