"""
population_router.py

FastAPI Router Layer
--------------------
Exposes Population Health Analytics APIs.

Responsibilities:
1. Receive HTTP Requests
2. Invoke Service Layer
3. Return JSON Responses
4. Handle HTTP Exceptions

Author: Healthcare Analytics Platform
"""

from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import status

from services.population_service import (
    PopulationAnalyticsService
)
from fastapi.responses import StreamingResponse

from visualizations.population_visualization_impl import (
    PopulationAnalyticsVisualization
)
router = APIRouter(
    prefix="/population",
    tags=["Population Health Analytics"]
)



# ------------------------------------------------------------------
# Population Summary
# ------------------------------------------------------------------

@router.get(
    "/summary",
    status_code=status.HTTP_200_OK
)
def get_population_summary():

    try:

        return {
            "success": True,
            "data": PopulationAnalyticsService.get_population_summary()
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )


# ------------------------------------------------------------------
# Age Distribution
# ------------------------------------------------------------------

@router.get(
    "/age-distribution",
    status_code=status.HTTP_200_OK
)
def get_age_distribution():

    try:

        return {
            "success": True,
            "data": PopulationAnalyticsService.get_age_distribution()
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )


# ------------------------------------------------------------------
# Gender Distribution
# ------------------------------------------------------------------

@router.get(
    "/gender-distribution",
    status_code=status.HTTP_200_OK
)
def get_gender_distribution():

    try:

        return {
            "success": True,
            "data": PopulationAnalyticsService.get_gender_distribution()
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )


# ------------------------------------------------------------------
# Smoking Analysis
# ------------------------------------------------------------------

@router.get(
    "/smoking",
    status_code=status.HTTP_200_OK
)
def get_smoking_analysis():

    try:

        return {
            "success": True,
            "data": PopulationAnalyticsService.get_smoking_analysis()
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )


# ------------------------------------------------------------------
# Alcohol Analysis
# ------------------------------------------------------------------

@router.get(
    "/alcohol",
    status_code=status.HTTP_200_OK
)
def get_alcohol_analysis():

    try:

        return {
            "success": True,
            "data": PopulationAnalyticsService.get_alcohol_analysis()
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )


# ------------------------------------------------------------------
# Exercise Analysis
# ------------------------------------------------------------------

@router.get(
    "/exercise",
    status_code=status.HTTP_200_OK
)
def get_exercise_analysis():

    try:

        return {
            "success": True,
            "data": PopulationAnalyticsService.get_exercise_analysis()
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )


# ------------------------------------------------------------------
# Obesity Analysis
# ------------------------------------------------------------------

@router.get(
    "/obesity",
    status_code=status.HTTP_200_OK
)
def get_obesity_analysis():

    try:

        return {
            "success": True,
            "data": PopulationAnalyticsService.get_obesity_analysis()
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )


# ------------------------------------------------------------------
# Hypertension Analysis
# ------------------------------------------------------------------

@router.get(
    "/hypertension",
    status_code=status.HTTP_200_OK
)
def get_hypertension_analysis():

    try:

        return {
            "success": True,
            "data": PopulationAnalyticsService.get_hypertension_analysis()
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )


# ------------------------------------------------------------------
# Diabetes Analysis
# ------------------------------------------------------------------

@router.get(
    "/diabetes",
    status_code=status.HTTP_200_OK
)
def get_diabetes_analysis():

    try:

        return {
            "success": True,
            "data": PopulationAnalyticsService.get_diabetes_analysis()
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )


# ------------------------------------------------------------------
# Top Risk Factors
# ------------------------------------------------------------------

@router.get(
    "/risk-factors",
    status_code=status.HTTP_200_OK
)
def get_top_risk_factors():

    try:

        return {
            "success": True,
            "data": PopulationAnalyticsService.get_top_risk_factors()
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )


# ------------------------------------------------------------------
# Dashboard
# ------------------------------------------------------------------
@router.get(
    "/dashboard-kpis"
)
def dashboard():

    image_stream = (
        PopulationAnalyticsService
        .dashboard()
    )

    return StreamingResponse(
        image_stream,
        media_type="image/png"
    )