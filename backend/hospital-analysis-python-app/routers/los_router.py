"""
los_router.py

Length of Stay (LOS) Analytics APIs

Author: Healthcare Analytics Platform
"""

from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import status

from services.los_service import (
    LOSAnalyticsService
)

router = APIRouter(
    prefix="/los",
    tags=["Length of Stay Analytics"]
)

from config.settings import (
    PATIENTS_FILE,
    OUTCOMES_FILE
)




# ==========================================================
# Service Initialization
# ==========================================================

los_service = LOSAnalyticsService(
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
            "data": los_service.get_dashboard_kpis()
        }

    except Exception as ex:
        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ==========================================================
# Average LOS
# ==========================================================

@router.get(
    "/average-los",
    status_code=status.HTTP_200_OK
)
def get_average_los():

    try:
        return {
            "success": True,
            "data": los_service.get_average_los()
        }

    except Exception as ex:
        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ==========================================================
# Median LOS
# ==========================================================

@router.get(
    "/median-los",
    status_code=status.HTTP_200_OK
)
def get_median_los():

    try:
        return {
            "success": True,
            "data": los_service.get_median_los()
        }

    except Exception as ex:
        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ==========================================================
# LOS By Age Group
# ==========================================================

@router.get(
    "/by-age-group",
    status_code=status.HTTP_200_OK
)
def get_los_by_age_group():

    try:
        return {
            "success": True,
            "data": los_service.get_los_by_age_group()
        }

    except Exception as ex:
        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ==========================================================
# LOS By Gender
# ==========================================================

@router.get(
    "/by-gender",
    status_code=status.HTTP_200_OK
)
def get_los_by_gender():

    try:
        return {
            "success": True,
            "data": los_service.get_los_by_gender()
        }

    except Exception as ex:
        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ==========================================================
# LOS By Disease
# ==========================================================

@router.get(
    "/by-disease",
    status_code=status.HTTP_200_OK
)
def get_los_by_disease():

    try:
        return {
            "success": True,
            "data": los_service.get_los_by_disease()
        }

    except Exception as ex:
        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ==========================================================
# LOS By Charlson Risk
# ==========================================================

@router.get(
    "/by-charlson",
    status_code=status.HTTP_200_OK
)
def get_los_by_charlson():

    try:
        return {
            "success": True,
            "data": los_service.get_los_by_charlson()
        }

    except Exception as ex:
        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ==========================================================
# LOS By ICU
# ==========================================================

@router.get(
    "/by-icu",
    status_code=status.HTTP_200_OK
)
def get_los_by_icu():

    try:
        return {
            "success": True,
            "data": los_service.get_los_by_icu()
        }

    except Exception as ex:
        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ==========================================================
# Long Stay Patients
# ==========================================================

@router.get(
    "/long-stay-patients",
    status_code=status.HTTP_200_OK
)
def get_long_stay_patients(
    top_n: int = 25
):

    try:
        return {
            "success": True,
            "data": los_service.get_long_stay_patients(
                top_n=top_n
            )
        }

    except Exception as ex:
        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ==========================================================
# LOS Summary
# ==========================================================

@router.get(
    "/summary",
    status_code=status.HTTP_200_OK
)
def get_los_summary():

    try:
        return {
            "success": True,
            "data": los_service.get_los_summary()
        }

    except Exception as ex:
        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )