from typing import List

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from cruds import managers
from database import get_db
from utils.sockets import notify_clients
from schemas.patients import PatientSchema, PatientSchemaCreate, PatientSchemaUpdate

router = APIRouter(prefix="/patients", tags=["patients"])


@router.post("/", response_model=PatientSchema)
async def create_patient(
    patient_schema: PatientSchemaCreate, db: Session = Depends(get_db)
):
    patient = managers.PatientCRUDManager(session=db).create(schema=patient_schema)
    await notify_clients(
        f"Создан Пациент '{patient.get_full_name()} (ID: {patient.id})'"
    )
    return patient


@router.get("/all", response_model=List[PatientSchema])
async def read_patients(db: Session = Depends(get_db)):
    patient = managers.PatientCRUDManager(session=db).get_all(db=db)
    return patient


@router.get("/", response_model=PatientSchema)
async def read_patient(patient_id: int, db: Session = Depends(get_db)):
    try:
        patient = managers.PatientCRUDManager(session=db).get_by_id(obj_id=patient_id)
        if patient is None:
            raise NoResultFound
        return patient
    except NoResultFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Patient not found"
        )


@router.patch("/", response_model=PatientSchema)
async def update_patient(
    patient_id: int, patient_schema: PatientSchemaUpdate, db: Session = Depends(get_db)
):
    try:
        patient = managers.PatientCRUDManager(session=db).update(
            obj_id=patient_id, schema=patient_schema
        )
        await notify_clients(
            f"Обновлён Пациент '{patient.get_full_name()} (ID: {patient.id})'"
        )
        return patient
    except NoResultFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Patient not found"
        )


@router.delete("/", status_code=status.HTTP_200_OK)
async def delete_patient(patient_id: int, db: Session = Depends(get_db)):
    try:
        patient = managers.PatientCRUDManager(session=db).delete(obj_id=patient_id)
        await notify_clients(
            f"Удалён Пациент '{patient.get_full_name()} (ID: {patient_id})'"
        )
        return patient
    except NoResultFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Patient not found"
        )
