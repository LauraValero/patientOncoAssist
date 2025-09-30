from typing import List, Optional
from app.core.database import supabase
from app.schemas.clinical_history import ClinicalHistoryCreate, ClinicalHistoryUpdate


class ClinicalHistoryService:
    TABLE_NAME = "clinical_histories"

    @staticmethod
    def get_clinical_history(history_id: int) -> Optional[dict]:
        response = (
            supabase.table(ClinicalHistoryService.TABLE_NAME)
            .select("*")
            .eq("id", history_id)
            .single()
            .execute()
        )
        return response.data if response.data else None

    @staticmethod
    def get_clinical_histories_by_document(document_id: str) -> List[dict]:
        response = (
            supabase.table(ClinicalHistoryService.TABLE_NAME)
            .select("*")
            .eq("document_id", document_id)   # cedula del paciente
            .execute()
        )
        return response.data or []

    @staticmethod
    def create_clinical_history(clinical_history_in: ClinicalHistoryCreate) -> dict:
        response = (
            supabase.table(ClinicalHistoryService.TABLE_NAME)
            .insert(clinical_history_in.dict())
            .execute()
        )
        if response.data:
            return response.data[0]
        return {}

    @staticmethod
    def update_clinical_history(history_id: int, clinical_history_in: ClinicalHistoryUpdate) -> Optional[dict]:
        response = (
            supabase.table(ClinicalHistoryService.TABLE_NAME)
            .update(clinical_history_in.dict(exclude_unset=True))
            .eq("id", history_id)
            .execute()
        )
        return response.data[0] if response.data else None

    @staticmethod
    def delete_clinical_history(history_id: int) -> bool:
        response = (
            supabase.table(ClinicalHistoryService.TABLE_NAME)
            .delete()
            .eq("id", history_id)
            .execute()
        )
        return bool(response.data)
