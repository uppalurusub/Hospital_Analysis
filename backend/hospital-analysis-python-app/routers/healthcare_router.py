from fastapi import APIRouter

from services.healthcare_service import (
    HealthcareAnalyticsService
)

router = APIRouter(
    prefix="/healthcare",
    tags=["Healthcare Analytics"]
)

@router.get("/load-and-validate")

def load_and_validate():

    return HealthcareAnalyticsService.load_datasets()