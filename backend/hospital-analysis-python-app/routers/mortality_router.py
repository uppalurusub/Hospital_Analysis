"""
mortality_router.py

Mortality Analytics APIs

Author: Healthcare Analytics Platform
"""

from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import status

from services.mortality_service import (
    MortalityAnalyticsService
)

from config.settings import (
    PATIENTS_FILE,
    OUTCOMES_FILE
)



router = APIRouter(
    prefix="/mortality",
    tags=["Mortality Analytics"]
)

# ==========================================================
# Service Initialization
# ==========================================================

mortality_service = MortalityAnalyticsService(
    patient_file_path=PATIENTS_FILE,
    outcome_file_path=OUTCOMES_FILE
)

# ==========================================================
# Dashboard KPIs
# ==========================================================

@router.get(
    "/dashboard-kpis",
    status_code=status.HTTP_200_OK
)
def get_dashboard_kpis():

    try:

        return {
            "success": True,
            "data": mortality_service.get_dashboard_kpis()
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ==========================================================
# Overall Mortality Rate
# ==========================================================

@router.get(
    "/rate",
    status_code=status.HTTP_200_OK
)
def get_mortality_rate():

    try:

        return {
            "success": True,
            "data": mortality_service.get_mortality_rate()
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ==========================================================
# Mortality By Age Group
# ==========================================================

@router.get(
    "/by-age-group",
    status_code=status.HTTP_200_OK
)
def get_mortality_by_age_group():

    try:

        return {
            "success": True,
            "data": mortality_service.get_mortality_by_age_group()
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ==========================================================
# Mortality By Gender
# ==========================================================

@router.get(
    "/by-gender",
    status_code=status.HTTP_200_OK
)
def get_mortality_by_gender():

    try:

        return {
            "success": True,
            "data": mortality_service.get_mortality_by_gender()
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ==========================================================
# Mortality By Charlson Risk
# ==========================================================

@router.get(
    "/by-charlson",
    status_code=status.HTTP_200_OK
)
def get_mortality_by_charlson():

    try:

        return {
            "success": True,
            "data": mortality_service.get_mortality_by_charlson()
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ==========================================================
# Mortality By ICU
# ==========================================================

@router.get(
    "/by-icu",
    status_code=status.HTTP_200_OK
)
def get_mortality_by_icu():

    try:

        return {
            "success": True,
            "data": mortality_service.get_mortality_by_icu()
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ==========================================================
# Mortality By Disease
# ==========================================================

@router.get(
    "/by-disease",
    status_code=status.HTTP_200_OK
)
def get_mortality_by_disease():

    try:

        return {
            "success": True,
            "data": mortality_service.get_mortality_by_disease()
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ==========================================================
# High Risk Mortality Patients
# ==========================================================

@router.get(
    "/high-risk-patients",
    status_code=status.HTTP_200_OK
)
def get_high_risk_patients(
    top_n: int = 25
):

    try:

        return {
            "success": True,
            "data": mortality_service.get_high_risk_patients(
                top_n=top_n
            )
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ==========================================================
# Mortality Risk Summary
# ==========================================================

@router.get(
    "/risk-summary",
    status_code=status.HTTP_200_OK
)
def get_risk_summary():

    try:

        return {
            "success": True,
            "data": mortality_service.get_risk_summary()
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )