from datetime import datetime, date
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class PersonSchemaBase(BaseModel):
    last_name: str
    first_name: str
    middle_name: Optional[str] = None
    contact_information: str
    birth_date: date

    # role: str


class PersonSchemaCreate(PersonSchemaBase):
    pass


class PersonSchemaUpdate(PersonSchemaBase):
    last_name: Optional[str] = None
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    contact_information: Optional[str] = None
    birth_date: Optional[date] = None

    # role: Optional[str] = None


class PersonSchema(PersonSchemaBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime
