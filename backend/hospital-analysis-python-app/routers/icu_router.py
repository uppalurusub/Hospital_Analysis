"""
icu_router.py

ICU Analytics REST APIs

Author: Healthcare Analytics Platform
"""

from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import status

from services.icu_service import (
    ICUAnalyticsService
)
from config.settings import (
    PATIENTS_FILE,
    OUTCOMES_FILE
)




router = APIRouter(
    prefix="/icu",
    tags=["ICU Analytics"]
)

# ==========================================================
# Service Initialization
# ==========================================================

icu_service = ICUAnalyticsService(
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
            "data": icu_service.get_dashboard_kpis()
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ==========================================================
# ICU Admission Rate
# ==========================================================

@router.get(
    "/admission-rate",
    status_code=status.HTTP_200_OK
)
def get_icu_admission_rate():

    try:

        return {
            "success": True,
            "data": icu_service.get_icu_admission_rate()
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ==========================================================
# Average ICU Days
# ==========================================================

@router.get(
    "/average-days",
    status_code=status.HTTP_200_OK
)
def get_average_icu_days():

    try:

        return {
            "success": True,
            "data": icu_service.get_average_icu_days()
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ==========================================================
# ICU By Age Group
# ==========================================================

@router.get(
    "/by-age-group",
    status_code=status.HTTP_200_OK
)
def get_icu_by_age_group():

    try:

        return {
            "success": True,
            "data": icu_service.get_icu_by_age_group()
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ==========================================================
# ICU By Gender
# ==========================================================

@router.get(
    "/by-gender",
    status_code=status.HTTP_200_OK
)
def get_icu_by_gender():

    try:

        return {
            "success": True,
            "data": icu_service.get_icu_by_gender()
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ==========================================================
# ICU By Charlson Risk
# ==========================================================

@router.get(
    "/by-charlson",
    status_code=status.HTTP_200_OK
)
def get_icu_by_charlson():

    try:

        return {
            "success": True,
            "data": icu_service.get_icu_by_charlson()
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ==========================================================
# ICU By Disease
# ==========================================================

@router.get(
    "/by-disease",
    status_code=status.HTTP_200_OK
)
def get_icu_by_disease():

    try:

        return {
            "success": True,
            "data": icu_service.get_icu_by_disease()
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ==========================================================
# High ICU Risk Patients
# ==========================================================

@router.get(
    "/high-risk-patients",
    status_code=status.HTTP_200_OK
)
def get_high_icu_risk_patients(
    top_n: int = 25
):

    try:

        return {
            "success": True,
            "data": icu_service.get_high_icu_risk_patients(
                top_n=top_n
            )
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ==========================================================
# ICU Risk Summary
# ==========================================================

@router.get(
    "/risk-summary",
    status_code=status.HTTP_200_OK
)
def get_icu_risk_summary():

    try:

        return {
            "success": True,
            "data": icu_service.get_icu_risk_summary()
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )