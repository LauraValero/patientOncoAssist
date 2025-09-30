from typing import List, Optional
from app.core.database import supabase
from app.schemas.patient import PatientCreate, PatientUpdate


class PatientService:
    TABLE_NAME = "patient"

    @staticmethod
    def create_patient(patient: PatientCreate) -> Optional[dict]:
        res = supabase.table(PatientService.TABLE_NAME).insert(patient.dict()).execute()
        if res.data:
            return res.data[0]
        return None

    @staticmethod
    def get_patient(document_id: str) -> Optional[dict]:
        res = supabase.table(PatientService.TABLE_NAME).select("*").eq("document_id", document_id).single().execute()
        return res.data

    @staticmethod
    def list_patients(page: int = None, page_size: int = None) -> List[dict]:
        query = supabase.table(PatientService.TABLE_NAME).select("*")
        if page is not None and page_size is not None:
            start = (page - 1) * page_size
            end = start + page_size - 1
            query = query.range(start, end)
        res = query.execute()
        return res.data or []

    @staticmethod
    def update_patient(document_id: str, patient_update: PatientUpdate) -> Optional[dict]:
        res = supabase.table(PatientService.TABLE_NAME).update(patient_update.dict(exclude_unset=True)).eq("document_id", document_id).execute()
        return res.data[0] if res.data else None

    @staticmethod
    def delete_patient(document_id: str) -> bool:
        res = supabase.table(PatientService.TABLE_NAME).delete().eq("document_id", document_id).execute()
        return bool(res.data)
