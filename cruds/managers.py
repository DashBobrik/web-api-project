from sqlalchemy.orm import Session

from cruds.crud import CRUDManager
from models import Doctor, Patient, MedicalService, Appointment


class PatientCRUDManager(CRUDManager):
    def __init__(self, session: Session = None):
        super().__init__(session=session, model=Patient)


class DoctorCRUDManager(CRUDManager):
    def __init__(self, session: Session = None):
        super().__init__(session=session, model=Doctor)


class RouteCRUDManager(CRUDManager):
    def __init__(self, session: Session = None):
        super().__init__(session=session, model=MedicalService)


class AppointmentCRUDManager(CRUDManager):
    def __init__(self, session: Session = None):
        super().__init__(session=session, model=Appointment)
