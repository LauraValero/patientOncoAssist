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
    family_history: FamilyHistory = Field(None, description="Indicates if there is a family history of cancer.")
    previous_cancer_history: PreviousCancerHistory = Field(None, description="Indicates if the patient has had cancer previously.")
    
    # Diagnosis information
    stage_at_diagnosis: StageAtDiagnosis = Field(..., description="Cancer stage at diagnosis.")
    tumor_aggressiveness: TumorAggressiveness = Field(..., description="Level of tumor aggressiveness.")
    
    # Screening and access
    colonoscopy_access: ColonoscopyAccess = Field(None, description="Indicates if the patient has access to colonoscopy.")
    screening_regularity: ScreeningRegularity = Field(None, description="Frequency or regularity of screening tests.")
    
    # Lifestyle factors
    diet_type: DietType = Field(None, description="Predominant diet type.")
    bmi: Decimal = Field(None, description="Body Mass Index (BMI) value.", ge=0, le=100)
    physical_activity_level: PhysicalActivityLevel = Field(None, description="Physical activity level.")
    smoking_status: SmokingStatus = Field(None, description="Patient's smoking status.")
    alcohol_consumption: AlcoholConsumption = Field(None, description="Level of alcohol consumption.")
    fiber_consumption: FiberConsumption = Field(None, description="Level of fiber consumption.")
    insurance_coverage: InsuranceCoverage = Field(None, description="Patient's insurance coverage status.")
    
    # Treatment information
    time_to_diagnosis: TimeToDiagnosis = Field(None, description="Timeliness of diagnosis.")
    treatment_access: TreatmentAccess = Field(..., description="Patient's access to treatments.")
    treatment_id: int = Field(None, description="ID of the recommended treatment.")
    chemotherapy_received: ChemotherapyReceived = Field(None, description="Indicates if chemotherapy was received.")
    radiotherapy_received: RadiotherapyReceived = Field(None, description="Indicates if radiotherapy was received.")
    surgery_received: SurgeryReceived = Field(None, description="Indicates if surgery was received.")
    treatment_recommendation: str = Field(None, description="AI treatment recommendation name.")
    
    # Follow-up and outcomes
    follow_up_adherence: FollowUpAdherence = Field(..., description="Degree of patient adherence to medical follow-up.")
    recurrence: Recurrence = Field(None, description="Indicates if cancer recurrence occurred.")
    time_to_recurrence: int = Field(None, description="Days until recurrence occurred.", ge=0)


class ClinicalHistoryCreate(ClinicalHistoryBase):
    document_id: str = Field(
        ..., description="Document ID of the patient."
    )
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
    family_history: FamilyHistory = None
    previous_cancer_history: PreviousCancerHistory = None
    stage_at_diagnosis: StageAtDiagnosis = None
    tumor_aggressiveness: TumorAggressiveness = None
    colonoscopy_access: ColonoscopyAccess = None
    screening_regularity: ScreeningRegularity = None
    diet_type: DietType = None
    bmi: Decimal = None
    physical_activity_level: PhysicalActivityLevel = None
    smoking_status: SmokingStatus = None
    alcohol_consumption: AlcoholConsumption = None
    fiber_consumption: FiberConsumption = None
    insurance_coverage: InsuranceCoverage = None
    time_to_diagnosis: TimeToDiagnosis = None
    treatment_access: TreatmentAccess = None
    treatment_id: int = None
    chemotherapy_received: ChemotherapyReceived = None
    radiotherapy_received: RadiotherapyReceived = None
    surgery_received: SurgeryReceived = None
    treatment_recommendation: str = None
    follow_up_adherence: FollowUpAdherence = None
    recurrence: Recurrence = None
    time_to_recurrence: int = None


class ClinicalHistoryRead(ClinicalHistoryBase):
    id: int = Field(..., description="Unique ID of the clinical history (primary key).")
    document_id: str = Field(..., description="Document ID of the patient.")
    created: datetime = Field(..., description="Date and time when the patient was created.")
    edited: datetime = Field(..., description="Date and time when the patient was last edited.")
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
