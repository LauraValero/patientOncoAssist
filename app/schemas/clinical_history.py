from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum
from datetime import datetime
from decimal import Decimal

class StageAtDiagnosis(str, Enum):
    I = "I"
    II = "II"
    III = "III"
    IV = "IV"

class TumorAggressiveness(str, Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"

class FollowUpAdherence(str, Enum):
    GOOD = "Good"
    POOR = "Poor"

class TreatmentAccess(str, Enum):
    ADEQUATE = "Adequate"
    LIMITED = "Limited"

class ScreeningRegularity(str, Enum):
    REGULAR = "Regular"
    IRREGULAR = "Irregular"
    NEVER = "Never"

class DietType(str, Enum):
    VEGETARIAN = "Vegetarian"
    VEGAN = "Vegan"
    OMNIVORE = "Omnivore"
    MEDITERRANEAN = "Mediterranean"
    WESTERN = "Western"

class PhysicalActivityLevel(str, Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"

class SmokingStatus(str, Enum):
    NEVER = "Never"
    CURRENT = "Current"
    FORMER = "Former"

class AlcoholConsumption(str, Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"

class FiberConsumption(str, Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"

class InsuranceCoverage(str, Enum):
    YES = "Yes"
    NO = "No"

class TimeToDiagnosis(str, Enum):
    DELAYED = "Delayed"
    TIMELY = "Timely"

class FamilyHistory(str, Enum):
    YES = "Yes"
    NO = "No"

class PreviousCancerHistory(str, Enum):
    YES = "Yes"
    NO = "No"

class ColonoscopyAccess(str, Enum):
    YES = "Yes"
    NO = "No"

class ChemotherapyReceived(str, Enum):
    YES = "Yes"
    NO = "No"

class RadiotherapyReceived(str, Enum):
    YES = "Yes"
    NO = "No"

class SurgeryReceived(str, Enum):
    YES = "Yes"
    NO = "No"

class Recurrence(str, Enum):
    YES = "Yes"
    NO = "No"

class ClinicalHistoryBase(BaseModel):
    # Family and personal history
    family_history: Optional[FamilyHistory] = Field(None, description="Indicates if there is a family history of cancer.")
    previous_cancer_history: Optional[PreviousCancerHistory] = Field(None, description="Indicates if the patient has had cancer previously.")
    
    # Diagnosis information
    stage_at_diagnosis: StageAtDiagnosis = Field(..., description="Cancer stage at diagnosis.")
    tumor_aggressiveness: TumorAggressiveness = Field(..., description="Level of tumor aggressiveness.")
    
    # Screening and access
    colonoscopy_access: Optional[ColonoscopyAccess] = Field(None, description="Indicates if the patient has access to colonoscopy.")
    screening_regularity: Optional[ScreeningRegularity] = Field(None, description="Frequency or regularity of screening tests.")
    
    # Lifestyle factors
    diet_type: Optional[DietType] = Field(None, description="Predominant diet type.")
    bmi: Optional[Decimal] = Field(None, description="Body Mass Index (BMI) value.", ge=0, le=100)
    physical_activity_level: Optional[PhysicalActivityLevel] = Field(None, description="Physical activity level.")
    smoking_status: Optional[SmokingStatus] = Field(None, description="Patient's smoking status.")
    alcohol_consumption: Optional[AlcoholConsumption] = Field(None, description="Level of alcohol consumption.")
    fiber_consumption: Optional[FiberConsumption] = Field(None, description="Level of fiber consumption.")
    insurance_coverage: Optional[InsuranceCoverage] = Field(None, description="Patient's insurance coverage status.")
    
    # Treatment information
    time_to_diagnosis: Optional[TimeToDiagnosis] = Field(None, description="Timeliness of diagnosis.")
    treatment_access: TreatmentAccess = Field(..., description="Patient's access to treatments.")
    treatment_id: Optional[int] = Field(None, description="ID of the recommended treatment.")
    chemotherapy_received: Optional[ChemotherapyReceived] = Field(None, description="Indicates if chemotherapy was received.")
    radiotherapy_received: Optional[RadiotherapyReceived] = Field(None, description="Indicates if radiotherapy was received.")
    surgery_received: Optional[SurgeryReceived] = Field(None, description="Indicates if surgery was received.")
    treatment_recommendation: Optional[str] = Field(None, description="AI treatment recommendation name.")
    
    # Follow-up and outcomes
    follow_up_adherence: FollowUpAdherence = Field(..., description="Degree of patient adherence to medical follow-up.")
    recurrence: Optional[Recurrence] = Field(None, description="Indicates if cancer recurrence occurred.")
    time_to_recurrence: Optional[int] = Field(None, description="Days until recurrence occurred.", ge=0)


class ClinicalHistoryCreate(ClinicalHistoryBase):
    document_id: str = Field(..., description="Document ID of the patient.")
    
    class Config:
        json_schema_extra = {
            "example": {
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
                "time_to_recurrence": 16,
            }
        }


class ClinicalHistoryUpdate(BaseModel):
    family_history: Optional[FamilyHistory] = None
    previous_cancer_history: Optional[PreviousCancerHistory] = None
    stage_at_diagnosis: Optional[StageAtDiagnosis] = None
    tumor_aggressiveness: Optional[TumorAggressiveness] = None
    colonoscopy_access: Optional[ColonoscopyAccess] = None
    screening_regularity: Optional[ScreeningRegularity] = None
    diet_type: Optional[DietType] = None
    bmi: Optional[Decimal] = None
    physical_activity_level: Optional[PhysicalActivityLevel] = None
    smoking_status: Optional[SmokingStatus] = None
    alcohol_consumption: Optional[AlcoholConsumption] = None
    fiber_consumption: Optional[FiberConsumption] = None
    insurance_coverage: Optional[InsuranceCoverage] = None
    time_to_diagnosis: Optional[TimeToDiagnosis] = None
    treatment_access: Optional[TreatmentAccess] = None
    treatment_id: Optional[int] = None
    chemotherapy_received: Optional[ChemotherapyReceived] = None
    radiotherapy_received: Optional[RadiotherapyReceived] = None
    surgery_received: Optional[SurgeryReceived] = None
    treatment_recommendation: Optional[str] = None
    follow_up_adherence: Optional[FollowUpAdherence] = None
    recurrence: Optional[Recurrence] = None
    time_to_recurrence: Optional[int] = None


class ClinicalHistoryRead(ClinicalHistoryBase):
    id: int = Field(..., description="Unique ID of the clinical history (primary key).")
    document_id: str = Field(..., description="Document ID of the patient.")
    created: datetime = Field(..., description="Date and time when the clinical history was created.")
    edited: datetime = Field(..., description="Date and time when the clinical history was last edited.")
    
    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
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
                "time_to_recurrence": 16,
                "created": "2025-09-23T10:15:30Z",
                "edited": "2025-09-23T10:15:30Z",
            }
        }