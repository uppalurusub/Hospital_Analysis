from pydantic import BaseModel
from typing import List

class DiseasePrevalence(BaseModel):
    disease: str
    patient_count: int
    prevalence_pct: float

class DiseasePrevalenceResponse(BaseModel):
    total_patients: int
    disease_summary: List[DiseasePrevalence]