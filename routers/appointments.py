from typing import List

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from cruds import managers
from database import get_db
from utils.sockets import notify_clients
from schemas.appointments import (
    AppointmentSchema,
    AppointmentSchemaCreate,
    AppointmentSchemaUpdate,
)

router = APIRouter(prefix="/appointments", tags=["appointments"])


@router.post("/", response_model=AppointmentSchema)
async def create_appointment(
    appointment_schema: AppointmentSchemaCreate, db: Session = Depends(get_db)
):
    appointment = managers.AppointmentCRUDManager(session=db).create(
        schema=appointment_schema
    )
    await notify_clients(
        f"Создан Приём '(ID: {appointment.id})' "
        f"Пациента '{appointment.patient.get_full_name()} (ID: {appointment.patient.id})' "
        f"к Доктору '{appointment.doctor.get_full_name()} (ID: {appointment.doctor.id})' "
        f"на услугу '{appointment.medical_service.name} / Цена: {appointment.medical_service.cost} (ID: {appointment.medical_service.id})'"
    )
    return appointment


@router.get("/all", response_model=List[AppointmentSchema])
async def read_appointments(db: Session = Depends(get_db)):
    appointment = managers.AppointmentCRUDManager(session=db).get_all(db=db)
    return appointment


@router.get("/", response_model=AppointmentSchema)
async def read_appointment(appointment_id: int, db: Session = Depends(get_db)):
    try:
        appointment = managers.AppointmentCRUDManager(session=db).get_by_id(
            obj_id=appointment_id
        )
        return appointment
    except NoResultFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Appointment not found"
        )


@router.patch("/", response_model=AppointmentSchema)
async def update_appointment(
    appointment_id: int,
    appointment_schema: AppointmentSchemaUpdate,
    db: Session = Depends(get_db),
):
    try:
        appointment = managers.AppointmentCRUDManager(session=db).update(
            obj_id=appointment_id, schema=appointment_schema
        )
        await notify_clients(
            f"Обновлён Приём '(ID: {appointment.id})' "
            f"Пациента '{appointment.patient.get_full_name()} (ID: {appointment.patient.id})' "
            f"к Доктору '{appointment.doctor.get_full_name()} (ID: {appointment.doctor.id})' "
            f"на услугу '{appointment.medical_service.name} / Цена: {appointment.medical_service.cost} (ID: {appointment.medical_service.id})'"
        )
        return appointment
    except NoResultFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Appointment not found"
        )


@router.delete("/", status_code=status.HTTP_200_OK)
async def delete_appointment(appointment_id: int, db: Session = Depends(get_db)):
    try:
        appointment = managers.AppointmentCRUDManager(session=db).delete(
            obj_id=appointment_id
        )
        await notify_clients(
            f"Удалён Приём '(ID: {appointment.id})' "
            f"Пациента '{appointment.patient.get_full_name()} (ID: {appointment.patient.id})' "
            f"к Доктору '{appointment.doctor.get_full_name()} (ID: {appointment.doctor.id})' "
            f"на услугу '{appointment.medical_service.name} / Цена: {appointment.medical_service.cost} (ID: {appointment.medical_service.id})'"
        )
        return appointment
    except NoResultFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Appointment not found"
        )
