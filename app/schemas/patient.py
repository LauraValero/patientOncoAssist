from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

class PatientBase(BaseModel):
    document_id: str = Field(..., description="Unique identification number of the patient.")
    name: str = Field(..., description="Full name of the patient.")
    age: int = Field(..., description="Age of the patient.", ge=0)
    email: EmailStr = Field(..., description="Patient's email address.")
    phone: Optional[str] = Field(None, description="Patient's phone number.")
    address: Optional[str] = Field(None, description="Patient's address.")

class PatientCreate(PatientBase):
    pass

class PatientUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    address: Optional[str] = None

class PatientRead(PatientBase):
    created: datetime = Field(..., description="Date and time when the patient was created.")
    edited: datetime = Field(..., description="Date and time when the patient was last edited.")