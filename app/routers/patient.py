from fastapi import APIRouter, HTTPException, status, Depends
from typing import List
from httpx import HTTPStatusError, RequestError

from app.schemas.patient import (
    PatientCreate,
    PatientRead,
    PatientUpdate,
)
from app.services.patient_service import PatientService
from app.core.security import require_token
from fastapi import Body

router = APIRouter(
    prefix="/patients",
    tags=["patients"],
)


def handle_http_error(e: HTTPStatusError):
    code = e.response.status_code
    if code == 400:
        raise HTTPException(status_code=400, detail="Bad request to database")
    elif code == 404:
        raise HTTPException(status_code=404, detail="Resource not found")
    elif code == 409:
        raise HTTPException(status_code=409, detail="Conflict: patient already exists")
    else:
        raise HTTPException(status_code=500, detail=f"Database error ({code}): {e.response.text}")


def handle_request_error(e: RequestError):
    raise HTTPException(status_code=503, detail=f"Database not reachable: {str(e)}")


@router.post(
    "/",
    response_model=PatientRead,
    status_code=status.HTTP_201_CREATED,
    responses={
        201: {"description": "Created"},
        400: {"description": "Bad Request - validation or business error"},
        401: {"description": "Authorization required"},
        403: {"description": "Invalid token"},
        409: {"description": "Conflict"},
        503: {"description": "Database or Auth service unavailable"},
    },
)
def create_patient(
    patient_in: PatientCreate = Body(
        ...,
        examples={
            "valid": {
                "summary": "Valid patient",
                "value": {
                    "document_id": "12345678",
                    "name": "Jane Doe",
                    "age": 42,
                    "email": "jane.doe@example.com",
                    "phone": "+57 300 123 4567",
                    "address": "Calle 123 #45-67, Bogotá",
                },
            },
            "invalid": {
                "summary": "Invalid types",
                "value": {
                    "document_id": 123,  # should be string
                    "name": 999,  # should be string
                    "age": -5,  # should be >= 0
                    "email": "not-an-email",
                },
            },
        },
    ),
    token_info: dict = Depends(require_token),
):
    """Create a new patient."""
    try:
        patient = PatientService.create_patient(patient_in)
        if not patient:
            raise HTTPException(status_code=400, detail="Could not create patient")
        return patient
    except HTTPStatusError as e:
        handle_http_error(e)
    except RequestError as e:
        handle_request_error(e)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


@router.get(
    "/{document_id}",
    response_model=PatientRead,
    responses={
        200: {"description": "OK"},
        401: {"description": "Authorization required"},
        403: {"description": "Invalid token"},
        404: {"description": "Patient not found"},
        503: {"description": "Database or Auth service unavailable"},
    },
)
def get_patient(document_id: str, token_info: dict = Depends(require_token)):
    """Get patient information by document ID."""
    try:
        patient = PatientService.get_patient(document_id)
        if not patient:
            raise HTTPException(status_code=404, detail="Patient not found")
        return patient
    except HTTPStatusError as e:
        handle_http_error(e)
    except RequestError as e:
        handle_request_error(e)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


@router.get(
    "/",
    response_model=List[PatientRead],
    responses={
        200: {"description": "OK"},
        401: {"description": "Authorization required"},
        403: {"description": "Invalid token"},
        503: {"description": "Database or Auth service unavailable"},
    },
)
def list_patients(page: int = None, page_size: int = None, token_info: dict = Depends(require_token)):
    """List patients (optional pagination)."""
    try:
        return PatientService.list_patients(page, page_size)
    except HTTPStatusError as e:
        handle_http_error(e)
    except RequestError as e:
        handle_request_error(e)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


@router.patch(
    "/{document_id}",
    response_model=PatientRead,
    responses={
        200: {"description": "OK"},
        400: {"description": "Bad Request - validation or business error"},
        401: {"description": "Authorization required"},
        403: {"description": "Invalid token"},
        404: {"description": "Patient not found"},
        503: {"description": "Database or Auth service unavailable"},
    },
)
def update_patient(document_id: str, patient_in: PatientUpdate, token_info: dict = Depends(require_token)):
    """Partially update a patient by document ID."""
    try:
        updated = PatientService.update_patient(document_id, patient_in)
        if not updated:
            raise HTTPException(status_code=404, detail="Patient not found")
        return updated
    except HTTPStatusError as e:
        handle_http_error(e)
    except RequestError as e:
        handle_request_error(e)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


@router.delete(
    "/{document_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        204: {"description": "No Content"},
        401: {"description": "Authorization required"},
        403: {"description": "Invalid token"},
        404: {"description": "Patient not found"},
        503: {"description": "Database or Auth service unavailable"},
    },
)
def delete_patient(document_id: str, token_info: dict = Depends(require_token)):
    """Delete a patient by document ID."""
    try:
        deleted = PatientService.delete_patient(document_id)
        if not deleted:
            raise HTTPException(status_code=404, detail="Patient not found")
        return None
    except HTTPStatusError as e:
        handle_http_error(e)
    except RequestError as e:
        handle_request_error(e)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
