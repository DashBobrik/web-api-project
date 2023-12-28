from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from schemas.persons import PersonSchemaBase


class DoctorSchemaBase(PersonSchemaBase):
    specialization: str


class DoctorSchemaCreate(DoctorSchemaBase):
    pass


class DoctorSchemaUpdate(DoctorSchemaBase):
    specialization: Optional[str] = None


class DoctorSchema(DoctorSchemaBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime
