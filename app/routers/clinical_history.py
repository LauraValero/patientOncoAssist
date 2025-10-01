from fastapi import APIRouter, HTTPException, status, Depends, Body
from typing import List
from httpx import HTTPStatusError, RequestError

from app.schemas.clinical_history import (
    ClinicalHistoryCreate,
    ClinicalHistoryRead,
    ClinicalHistoryUpdate,
)
from app.services.clinical_history_service import ClinicalHistoryService
from app.core.security import require_token

router = APIRouter(
    prefix="/clinical_histories",
    tags=["clinical_histories"],
)


def handle_http_error(e: HTTPStatusError):
    code = e.response.status_code
    if code == 404:
        raise HTTPException(status_code=404, detail="Clinical history not found")
    elif code == 400:
        raise HTTPException(status_code=400, detail="Bad request to database")
    else:
        raise HTTPException(status_code=500, detail=f"Database error ({code}): {e.response.text}")


def handle_request_error(e: RequestError):
    raise HTTPException(status_code=503, detail=f"Database not reachable: {str(e)}")


@router.get(
    "/{history_id}",
    response_model=ClinicalHistoryRead,
    responses={
        200: {"description": "OK"},
        401: {"description": "Authorization required"},
        403: {"description": "Invalid token"},
        404: {"description": "Clinical history not found"},
        503: {"description": "Database or Auth service unavailable"},
    },
)
def get_clinical_history(history_id: int, token_info: dict = Depends(require_token)):
    """Get a clinical history by ID."""
    try:
        history = ClinicalHistoryService.get_clinical_history(history_id)
        if not history:
            raise HTTPException(status_code=404, detail="Clinical history not found")
        return history
    except HTTPStatusError as e:
        handle_http_error(e)
    except RequestError as e:
        handle_request_error(e)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


@router.get(
    "/document/{document_id}",
    response_model=List[ClinicalHistoryRead],
    responses={
        200: {"description": "OK"},
        401: {"description": "Authorization required"},
        403: {"description": "Invalid token"},
        503: {"description": "Database or Auth service unavailable"},
    },
)
def get_histories_by_document(document_id: str, token_info: dict = Depends(require_token)):
    """Get all clinical histories by patient document ID."""
    try:
        return ClinicalHistoryService.get_clinical_histories_by_document(document_id)
    except HTTPStatusError as e:
        handle_http_error(e)
    except RequestError as e:
        handle_request_error(e)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


@router.post(
    "/",
    response_model=ClinicalHistoryRead,
    status_code=status.HTTP_201_CREATED,
    responses={
        201: {"description": "Created"},
        400: {"description": "Bad Request - validation or business error"},
        401: {"description": "Authorization required"},
        403: {"description": "Invalid token"},
        503: {"description": "Database or Auth service unavailable"},
    },
)
def create_clinical_history(
    clinical_history_in: ClinicalHistoryCreate = Body(
        ...,
        examples={
            "complete": {
                "summary": "Complete clinical history with all fields",
                "value": {
                    "document_id": "12345678",
                    "family_history": "Yes",
                    "previous_cancer_history": "No",
                    "stage_at_diagnosis": "III",
                    "tumor_aggressiveness": "High",
                    "colonoscopy_access": "No",
                    "screening_regularity": "Regular",
                    "diet_type": "Western",
                    "bmi": 33.0,
                    "physical_activity_level": "Low",
                    "smoking_status": "Never",
                    "alcohol_consumption": "Low",
                    "fiber_consumption": "Low",
                    "insurance_coverage": "Yes",
                    "time_to_diagnosis": "Delayed",
                    "treatment_access": "Adequate",
                    "treatment_id": 10,
                    "chemotherapy_received": "Yes",
                    "radiotherapy_received": "No",
                    "surgery_received": "No",
                    "treatment_recommendation": "T2",
                    "follow_up_adherence": "Good",
                    "recurrence": "No",
                    "time_to_recurrence": 16
                },
            },
            "minimal": {
                "summary": "Minimal required fields only",
                "value": {
                    "document_id": "87654321",
                    "stage_at_diagnosis": "II",
                    "tumor_aggressiveness": "Medium",
                    "treatment_access": "Adequate",
                    "follow_up_adherence": "Good"
                },
            },
            "invalid": {
                "summary": "Invalid types",
                "value": {
                    "document_id": 999,
                    "stage_at_diagnosis": "Stage5",
                    "tumor_aggressiveness": 1,
                    "follow_up_adherence": None,
                    "treatment_access": {},
                    "treatment_id": "abc"
                },
            },
        },
    ),
    token_info: dict = Depends(require_token),
):
    """Create a new clinical history."""
    try:
        history = ClinicalHistoryService.create_clinical_history(clinical_history_in)
        if not history:
            raise HTTPException(status_code=400, detail="Could not create clinical history")
        return history
    except HTTPStatusError as e:
        handle_http_error(e)
    except RequestError as e:
        handle_request_error(e)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


@router.patch(
    "/{history_id}",
    response_model=ClinicalHistoryRead,
    responses={
        200: {"description": "OK"},
        400: {"description": "Bad Request - validation or business error"},
        401: {"description": "Authorization required"},
        403: {"description": "Invalid token"},
        404: {"description": "Clinical history not found"},
        503: {"description": "Database or Auth service unavailable"},
    },
)
def update_clinical_history(history_id: int, clinical_history_in: ClinicalHistoryUpdate, token_info: dict = Depends(require_token)):
    """Partially update an existing clinical history."""
    try:
        updated = ClinicalHistoryService.update_clinical_history(history_id, clinical_history_in)
        if not updated:
            raise HTTPException(status_code=404, detail="Clinical history not found")
        return updated
    except HTTPStatusError as e:
        handle_http_error(e)
    except RequestError as e:
        handle_request_error(e)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


@router.delete(
    "/{history_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        204: {"description": "No Content"},
        401: {"description": "Authorization required"},
        403: {"description": "Invalid token"},
        404: {"description": "Clinical history not found"},
        503: {"description": "Database or Auth service unavailable"},
    },
)
def delete_clinical_history(history_id: int, token_info: dict = Depends(require_token)):
    """Delete a clinical history by ID."""
    try:
        deleted = ClinicalHistoryService.delete_clinical_history(history_id)
        if not deleted:
            raise HTTPException(status_code=404, detail="Clinical history not found")
        return None
    except HTTPStatusError as e:
        handle_http_error(e)
    except RequestError as e:
        handle_request_error(e)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
