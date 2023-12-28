from datetime import datetime
from typing import Optional

from pydantic import ConfigDict

from schemas.persons import PersonSchemaBase


class PatientSchemaBase(PersonSchemaBase):
    insurance_number: str


class PatientSchemaCreate(PatientSchemaBase):
    pass


class PatientSchemaUpdate(PatientSchemaBase):
    insurance_number: Optional[str] = None


class PatientSchema(PatientSchemaBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime
