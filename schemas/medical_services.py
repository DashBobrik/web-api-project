from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class MedicalServiceSchemaBase(BaseModel):
    name: str
    description: str
    cost: float


class MedicalServiceSchemaCreate(MedicalServiceSchemaBase):
    pass


class MedicalServiceSchemaUpdate(MedicalServiceSchemaBase):
    name: Optional[str] = None
    description: Optional[str] = None
    cost: Optional[float] = None


class MedicalServiceSchema(MedicalServiceSchemaBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime
