from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class AppointmentSchemaBase(BaseModel):
    appointment_time: datetime
    doctor_id: int
    patient_id: int
    medical_service_id: int


class AppointmentSchemaCreate(AppointmentSchemaBase):
    pass


class AppointmentSchemaUpdate(AppointmentSchemaBase):
    appointment_time: Optional[datetime] = None
    doctor_id: Optional[int] = None
    patient_id: Optional[int] = None
    medical_service_id: Optional[int] = None


class AppointmentSchema(AppointmentSchemaBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime
