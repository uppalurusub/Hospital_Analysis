from pydantic import BaseModel
from typing import Dict

class DatasetValidationResponse(BaseModel):
    row_count: int
    column_count: int
    duplicate_count: int

class LoadDataResponse(BaseModel):
    datasets: Dict