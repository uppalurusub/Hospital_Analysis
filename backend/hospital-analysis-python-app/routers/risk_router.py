"""
risk_router.py

Clinical Risk Analytics APIs

Author: Healthcare Analytics Platform
"""

from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import status

from services.risk_service import (
    RiskAnalyticsService
)

from config.settings import (
    PATIENTS_FILE,
    LAB_RESULTS_FILE,
    MEDICATIONS_FILE
)



router = APIRouter(
    prefix="/risk",
    tags=["Clinical Risk Analytics"]
)

# ==========================================================
# Service Initialization
# ==========================================================

risk_service = RiskAnalyticsService(

    patient_file_path=PATIENTS_FILE,
    lab_file_path=LAB_RESULTS_FILE,
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
            "data": risk_service.get_dashboard_kpis()
        }

    except Exception as ex:
        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ==========================================================
# High Blood Pressure Rate
# ==========================================================

@router.get(
    "/high-bp-rate",
    status_code=status.HTTP_200_OK
)
def get_high_bp_rate():

    try:
        return {
            "success": True,
            "data": risk_service.get_high_bp_rate()
        }

    except Exception as ex:
        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ==========================================================
# Obesity Rate
# ==========================================================

@router.get(
    "/obesity-rate",
    status_code=status.HTTP_200_OK
)
def get_obesity_rate():

    try:
        return {
            "success": True,
            "data": risk_service.get_obesity_rate()
        }

    except Exception as ex:
        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ==========================================================
# Tachycardia Rate
# ==========================================================

@router.get(
    "/tachycardia-rate",
    status_code=status.HTTP_200_OK
)
def get_tachycardia_rate():

    try:
        return {
            "success": True,
            "data": risk_service.get_tachycardia_rate()
        }

    except Exception as ex:
        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ==========================================================
# Abnormal Lab Rate
# ==========================================================

@router.get(
    "/abnormal-lab-rate",
    status_code=status.HTTP_200_OK
)
def get_abnormal_lab_rate():

    try:
        return {
            "success": True,
            "data": risk_service.get_abnormal_lab_rate()
        }

    except Exception as ex:
        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ==========================================================
# Medication Non-Adherence Rate
# ==========================================================

@router.get(
    "/medication-non-adherence",
    status_code=status.HTTP_200_OK
)
def get_medication_non_adherence():

    try:
        return {
            "success": True,
            "data": risk_service.get_medication_non_adherence_rate()
        }

    except Exception as ex:
        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ==========================================================
# Charlson Risk Distribution
# ==========================================================

@router.get(
    "/charlson-risk",
    status_code=status.HTTP_200_OK
)
def get_charlson_risk():

    try:
        return {
            "success": True,
            "data": risk_service.get_charlson_risk_distribution()
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
def get_high_risk_patients():

    try:
        return {
            "success": True,
            "data": risk_service.get_high_risk_patients()
        }

    except Exception as ex:
        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ==========================================================
# Risk Factor Summary
# ==========================================================

@router.get(
    "/risk-factor-summary",
    status_code=status.HTTP_200_OK
)
def get_risk_factor_summary():

    try:
        return {
            "success": True,
            "data": risk_service.get_risk_factor_summary()
        }

    except Exception as ex:
        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ==========================================================
# Population Risk Score
# ==========================================================

@router.get(
    "/population-risk-score",
    status_code=status.HTTP_200_OK
)
def get_population_risk_score():

    try:
        return {
            "success": True,
            "data": risk_service.get_population_risk_score()
        }

    except Exception as ex:
        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )