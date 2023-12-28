from typing import List

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from cruds import managers
from database import get_db
from utils.sockets import notify_clients
from schemas.doctors import DoctorSchema, DoctorSchemaCreate, DoctorSchemaUpdate

router = APIRouter(prefix="/doctors", tags=["doctors"])


@router.post("/", response_model=DoctorSchema)
async def create_doctor(
    doctor_schema: DoctorSchemaCreate, db: Session = Depends(get_db)
):
    doctor = managers.DoctorCRUDManager(session=db).create(schema=doctor_schema)
    await notify_clients(f"Создан Доктор '{doctor.get_full_name()} (ID: {doctor.id})'")
    return doctor


@router.get("/all", response_model=List[DoctorSchema])
async def read_doctors(db: Session = Depends(get_db)):
    doctor = managers.DoctorCRUDManager(session=db).get_all(db=db)
    return doctor


@router.get("/", response_model=DoctorSchema)
async def read_doctor(doctor_id: int, db: Session = Depends(get_db)):
    try:
        doctor = managers.DoctorCRUDManager(session=db).get_by_id(obj_id=doctor_id)
        if doctor is None:
            raise NoResultFound
        return doctor
    except NoResultFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Doctor not found"
        )


@router.patch("/", response_model=DoctorSchema)
async def update_doctor(
    doctor_id: int, doctor_schema: DoctorSchemaUpdate, db: Session = Depends(get_db)
):
    try:
        doctor = managers.DoctorCRUDManager(session=db).update(
            obj_id=doctor_id, schema=doctor_schema
        )
        await notify_clients(
            f"Обновлён Доктор '{doctor.get_full_name()} (ID: {doctor.id})'"
        )
        return doctor
    except NoResultFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Doctor not found"
        )


@router.delete("/", status_code=status.HTTP_200_OK)
async def delete_doctor(doctor_id: int, db: Session = Depends(get_db)):
    try:
        doctor = managers.DoctorCRUDManager(session=db).delete(obj_id=doctor_id)
        await notify_clients(
            f"Удалён Доктор '{doctor.get_full_name()} (ID: {doctor_id})'"
        )
        return doctor
    except NoResultFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Doctor not found"
        )
