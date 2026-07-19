"""
medication_router.py

Medication Analytics APIs

Author: Healthcare Analytics Platform
"""

from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import status

from services.medication_service import (
    MedicationAnalyticsService
)

from config.settings import (
    MEDICATIONS_FILE,
)



router = APIRouter(
    prefix="/medication",
    tags=["Medication Analytics"]
)

# ==========================================================
# Service Initialization
# ==========================================================

medication_service = MedicationAnalyticsService(
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

        return {
            "success": True,
            "data": medication_service.get_dashboard_kpis()
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ==========================================================
# Overall Adherence Rate
# ==========================================================

@router.get(
    "/adherence-rate",
    status_code=status.HTTP_200_OK
)
def get_adherence_rate():

    try:

        return {
            "success": True,
            "data": medication_service.get_adherence_rate()
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ==========================================================
# Non-Adherence Rate
# ==========================================================

@router.get(
    "/non-adherence-rate",
    status_code=status.HTTP_200_OK
)
def get_non_adherence_rate():

    try:

        return {
            "success": True,
            "data": medication_service.get_non_adherence_rate()
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ==========================================================
# Top Medications
# ==========================================================

@router.get(
    "/top-medications",
    status_code=status.HTTP_200_OK
)
def get_top_medications():

    try:

        return {
            "success": True,
            "data": medication_service.get_top_medications()
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ==========================================================
# Adherence By Medication
# ==========================================================

@router.get(
    "/adherence-by-medication",
    status_code=status.HTTP_200_OK
)
def get_adherence_by_medication():

    try:

        return {
            "success": True,
            "data": medication_service.get_adherence_by_medication()
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ==========================================================
# Adherence By Indication
# ==========================================================

@router.get(
    "/adherence-by-indication",
    status_code=status.HTTP_200_OK
)
def get_adherence_by_indication():

    try:

        return {
            "success": True,
            "data": medication_service.get_adherence_by_indication()
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ==========================================================
# Generic vs Brand Analysis
# ==========================================================

@router.get(
    "/generic-vs-brand",
    status_code=status.HTTP_200_OK
)
def get_generic_vs_brand():

    try:

        return {
            "success": True,
            "data": medication_service.get_generic_vs_brand()
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ==========================================================
# High Risk Non-Adherent Patients
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
            "data": medication_service.get_high_risk_patients(
                top_n=top_n
            )
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ==========================================================
# Medication Summary
# ==========================================================

@router.get(
    "/summary",
    status_code=status.HTTP_200_OK
)
def get_medication_summary():

    try:

        return {
            "success": True,
            "data": medication_service.get_medication_summary()
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )