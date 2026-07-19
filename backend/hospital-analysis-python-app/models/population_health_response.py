from pydantic import BaseModel
from typing import Dict, List


class PopulationHealthResponse(BaseModel):

    total_patients: int

    age_statistics: Dict

    age_distribution: Dict

    gender_mix: Dict

    bmi_categories: Dict

    smoking_rate: Dict

    alcohol_usage_rate: Dict

    exercise_compliance: Dict

    charlson_distribution: Dict