from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime
from enum import Enum

class Gender(str, Enum):
    MALE = "Male"
    FEMALE = "Female"
    OTHER = "Other"



class UrbanOrRural(str, Enum):
    URBAN = "Urban"
    RURAL = "Rural"

class PatientBase(BaseModel):
    document_id: str = Field(..., description="Unique identification number of the patient.")
    name: str = Field(..., description="Full name of the patient.")
    age: int = Field(..., description="Age of the patient.", ge=0)
    gender: Gender = Field(..., description="Patient's gender.")
    race: Optional[str] = Field(None, description="Patient's race.")
    region: Optional[str] = Field(None, description="Patient's region.")
    urban_or_rural: Optional[UrbanOrRural] = Field(None, description="Whether patient is from urban or rural area.")
    email: EmailStr = Field(..., description="Patient's email address.")
    phone: Optional[str] = Field(None, description="Patient's phone number.")
    address: Optional[str] = Field(None, description="Patient's address.")

class PatientCreate(PatientBase):
    pass

class PatientUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[Gender] = None
    race: Optional[str] = None
    region: Optional[str] = None
    urban_or_rural: Optional[UrbanOrRural] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    address: Optional[str] = None

class PatientRead(PatientBase):
    created: datetime = Field(..., description="Date and time when the patient was created.")
    edited: datetime = Field(..., description="Date and time when the patient was last edited.")