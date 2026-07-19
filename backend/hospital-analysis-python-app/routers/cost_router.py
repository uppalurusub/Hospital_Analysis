"""
cost_router.py

Healthcare Cost Analytics APIs

Author: Healthcare Analytics Platform
"""

from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import status

from services.cost_service import (
    CostAnalyticsService
)
from config.settings import (
    PATIENTS_FILE,
    OUTCOMES_FILE
)



router = APIRouter(
    prefix="/cost",
    tags=["Cost Analytics"]
)

# ==========================================================
# Service Initialization
# ==========================================================

cost_service = CostAnalyticsService(
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
            "data": cost_service.get_dashboard_kpis()
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ==========================================================
# Average Cost
# ==========================================================

@router.get(
    "/average-cost",
    status_code=status.HTTP_200_OK
)
def get_average_cost():

    try:

        return {
            "success": True,
            "data": cost_service.get_average_cost()
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ==========================================================
# Median Cost
# ==========================================================

@router.get(
    "/median-cost",
    status_code=status.HTTP_200_OK
)
def get_median_cost():

    try:

        return {
            "success": True,
            "data": cost_service.get_median_cost()
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ==========================================================
# Total Cost
# ==========================================================

@router.get(
    "/total-cost",
    status_code=status.HTTP_200_OK
)
def get_total_cost():

    try:

        return {
            "success": True,
            "data": cost_service.get_total_cost()
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ==========================================================
# Cost By Age Group
# ==========================================================

@router.get(
    "/by-age-group",
    status_code=status.HTTP_200_OK
)
def get_cost_by_age_group():

    try:

        return {
            "success": True,
            "data": cost_service.get_cost_by_age_group()
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ==========================================================
# Cost By Gender
# ==========================================================

@router.get(
    "/by-gender",
    status_code=status.HTTP_200_OK
)
def get_cost_by_gender():

    try:

        return {
            "success": True,
            "data": cost_service.get_cost_by_gender()
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ==========================================================
# Cost By Disease
# ==========================================================

@router.get(
    "/by-disease",
    status_code=status.HTTP_200_OK
)
def get_cost_by_disease():

    try:

        return {
            "success": True,
            "data": cost_service.get_cost_by_disease()
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ==========================================================
# Cost By Charlson Risk
# ==========================================================

@router.get(
    "/by-charlson",
    status_code=status.HTTP_200_OK
)
def get_cost_by_charlson():

    try:

        return {
            "success": True,
            "data": cost_service.get_cost_by_charlson()
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ==========================================================
# Cost By ICU
# ==========================================================

@router.get(
    "/by-icu",
    status_code=status.HTTP_200_OK
)
def get_cost_by_icu():

    try:

        return {
            "success": True,
            "data": cost_service.get_cost_by_icu()
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ==========================================================
# LOS Cost Analysis
# ==========================================================

@router.get(
    "/los-analysis",
    status_code=status.HTTP_200_OK
)
def get_cost_los_analysis():

    try:

        return {
            "success": True,
            "data": cost_service.get_cost_los_analysis()
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ==========================================================
# High Cost Patients
# ==========================================================

@router.get(
    "/high-cost-patients",
    status_code=status.HTTP_200_OK
)
def get_high_cost_patients(
    top_n: int = 25
):

    try:

        return {
            "success": True,
            "data": cost_service.get_high_cost_patients(
                top_n=top_n
            )
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ==========================================================
# Cost Summary
# ==========================================================

@router.get(
    "/summary",
    status_code=status.HTTP_200_OK
)
def get_cost_summary():

    try:

        return {
            "success": True,
            "data": cost_service.get_cost_summary()
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )