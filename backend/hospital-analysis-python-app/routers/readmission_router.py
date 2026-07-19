"""
readmission_router.py

Readmission Analytics REST APIs

Author: Healthcare Analytics Platform
"""

from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import status

from services.readmission_service import (
    ReadmissionAnalyticsService
)

from utils.json_sanitizer import sanitize_json
from config.settings import (
    PATIENTS_FILE,
    MEDICATIONS_FILE,
    OUTCOMES_FILE
)


router = APIRouter(
    prefix="/readmission",
    tags=["Readmission Analytics"]
)

# ==========================================================
# Service Initialization
# ==========================================================

readmission_service = ReadmissionAnalyticsService(
    patient_file_path=PATIENTS_FILE,
    outcome_file_path=OUTCOMES_FILE,
    medication_file_path=MEDICATIONS_FILE
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

        result = readmission_service.get_dashboard_kpis()

        return {
            "success": True,
            "data": sanitize_json(result)
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ==========================================================
# Readmission Rate
# ==========================================================

@router.get(
    "/rate",
    status_code=status.HTTP_200_OK
)
def get_readmission_rate():

    try:

        result = readmission_service.get_readmission_rate()

        return {
            "success": True,
            "data": sanitize_json(result)
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ==========================================================
# Average Days To Readmission
# ==========================================================

@router.get(
    "/average-days",
    status_code=status.HTTP_200_OK
)
def get_average_days_to_readmission():

    try:

        result = readmission_service.get_average_days_to_readmission()

        return {
            "success": True,
            "data": sanitize_json(result)
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ==========================================================
# Readmission By Age Group
# ==========================================================

@router.get(
    "/by-age-group",
    status_code=status.HTTP_200_OK
)
def get_readmission_by_age_group():

    try:

        result = readmission_service.get_readmission_by_age_group()

        return {
            "success": True,
            "data": sanitize_json(result)
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ==========================================================
# Readmission By Charlson Risk
# ==========================================================

@router.get(
    "/by-charlson",
    status_code=status.HTTP_200_OK
)
def get_readmission_by_charlson():

    try:

        result = readmission_service.get_readmission_by_charlson()
        return {
            "success": True,
            "data": sanitize_json(result)
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ==========================================================
# Readmission By Medication Adherence
# ==========================================================

@router.get(
    "/by-adherence",
    status_code=status.HTTP_200_OK
)
def get_readmission_by_adherence():

    try:

        result = readmission_service.get_readmission_by_adherence()

        return {
            "success": True,
            "data": sanitize_json(result)
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ==========================================================
# High Risk Patients
# ==========================================================

@router.get(
    "/high-risk-patients",
    status_code=status.HTTP_200_OK
)
def get_high_risk_patients(
    top_n: int = 25
):

    try:

        result = readmission_service.get_high_readmission_risk_patients(
                top_n=top_n
            )
        return {
            "success": True,
            "data": sanitize_json(result)
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ==========================================================
# Readmission Risk Summary
# ==========================================================

@router.get(
    "/risk-summary",
    status_code=status.HTTP_200_OK
)
def get_readmission_risk_summary():

    try:

        result = readmission_service.get_readmission_risk_summary()

        return {
            "success": True,
            "data": sanitize_json(result)
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )