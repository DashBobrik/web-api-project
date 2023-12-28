from fastapi import APIRouter

from routers.patients import router as patients_router
from routers.appointments import router as appointments_router
from routers.medical_services import router as routes_router
from routers.doctors import router as doctors_router

router = APIRouter(prefix="/v1")

router.include_router(patients_router)
router.include_router(doctors_router)
router.include_router(routes_router)
router.include_router(appointments_router)
