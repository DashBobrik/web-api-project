from typing import List

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from cruds import managers
from database import get_db
from utils.sockets import notify_clients
from schemas.medical_services import (
    MedicalServiceSchema,
    MedicalServiceSchemaCreate,
    MedicalServiceSchemaUpdate,
)

router = APIRouter(prefix="/medical_services", tags=["medical_services"])


@router.post("/", response_model=MedicalServiceSchema)
async def create_medical_service(
    medical_service_schema: MedicalServiceSchemaCreate, db: Session = Depends(get_db)
):
    medical_service = managers.RouteCRUDManager(session=db).create(
        schema=medical_service_schema
    )
    await notify_clients(
        f"Создана Медицинская улуга '{medical_service.name} / Цена: {medical_service.cost} (ID: {medical_service.id})'"
    )
    return medical_service


@router.get("/all", response_model=List[MedicalServiceSchema])
async def read_medical_services(db: Session = Depends(get_db)):
    medical_service = managers.RouteCRUDManager(session=db).get_all(db=db)
    return medical_service


@router.get("/", response_model=MedicalServiceSchema)
async def read_medical_service(medical_service_id: int, db: Session = Depends(get_db)):
    try:
        medical_service = managers.RouteCRUDManager(session=db).get_by_id(
            obj_id=medical_service_id
        )
        return medical_service
    except NoResultFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="MedicalService not found"
        )


@router.patch("/", response_model=MedicalServiceSchema)
async def update_medical_service(
    medical_service_id: int,
    medical_service_schema: MedicalServiceSchemaUpdate,
    db: Session = Depends(get_db),
):
    try:
        medical_service = managers.RouteCRUDManager(session=db).update(
            obj_id=medical_service_id, schema=medical_service_schema
        )
        await notify_clients(
            f"Обновлена Медицинская улуга '{medical_service.name} / Цена: {medical_service.cost} (ID: {medical_service.id})'"
        )
        return medical_service
    except NoResultFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="MedicalService not found"
        )


@router.delete("/", status_code=status.HTTP_200_OK)
async def delete_medical_service(medical_service_id: int, db: Session = Depends(get_db)):
    try:
        medical_service = managers.RouteCRUDManager(session=db).delete(
            obj_id=medical_service_id
        )
        await notify_clients(
            f"Удалена Медицинская улуга '{medical_service.name} / Цена: {medical_service.cost} (ID: {medical_service.id})'"
        )
        return medical_service
    except NoResultFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="MedicalService not found"
        )
