from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import status

from services.disease_service import (
    DiseaseService
)

from fastapi.responses import StreamingResponse

router = APIRouter(
    prefix="/disease",
    tags=["Disease Analytics"]
)


# ============================================================
# Top Diseases
# ============================================================

@router.get(
    "/top-diseases",
    status_code=status.HTTP_200_OK
)
def get_top_diseases():

    try:

        return {
            "success": True,
            "data": DiseaseService.get_top_diseases()
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ============================================================
# Hypertension
# ============================================================

@router.get(
    "/hypertension",
    status_code=status.HTTP_200_OK
)
def get_hypertension_prevalence():

    try:

        return {
            "success": True,
            "data": DiseaseService.get_hypertension_prevalence()
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ============================================================
# Type 2 Diabetes
# ============================================================

@router.get(
    "/type2-diabetes",
    status_code=status.HTTP_200_OK
)
def get_type2_diabetes_prevalence():

    try:

        return {
            "success": True,
            "data": DiseaseService.get_type2_diabetes_prevalence()
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ============================================================
# CKD
# ============================================================

@router.get(
    "/chronic-kidney-disease",
    status_code=status.HTTP_200_OK
)
def get_ckd_prevalence():

    try:

        return {
            "success": True,
            "data": DiseaseService.get_ckd_prevalence()
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ============================================================
# CAD
# ============================================================

@router.get(
    "/coronary-artery-disease",
    status_code=status.HTTP_200_OK
)
def get_cad_prevalence():

    try:

        return {
            "success": True,
            "data": DiseaseService.get_cad_prevalence()
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ============================================================
# Heart Failure
# ============================================================

@router.get(
    "/heart-failure",
    status_code=status.HTTP_200_OK
)
def get_heart_failure_prevalence():

    try:

        return {
            "success": True,
            "data": DiseaseService.get_heart_failure_prevalence()
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ============================================================
# COPD
# ============================================================

@router.get(
    "/copd",
    status_code=status.HTTP_200_OK
)
def get_copd_prevalence():

    try:

        return {
            "success": True,
            "data": DiseaseService.get_copd_prevalence()
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ============================================================
# Asthma
# ============================================================

@router.get(
    "/asthma",
    status_code=status.HTTP_200_OK
)
def get_asthma_prevalence():

    try:

        return {
            "success": True,
            "data": DiseaseService.get_asthma_prevalence()
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ============================================================
# Depression
# ============================================================

@router.get(
    "/depression",
    status_code=status.HTTP_200_OK
)
def get_depression_prevalence():

    try:

        return {
            "success": True,
            "data": DiseaseService.get_depression_prevalence()
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ============================================================
# Anxiety
# ============================================================

@router.get(
    "/anxiety",
    status_code=status.HTTP_200_OK
)
def get_anxiety_prevalence():

    try:

        return {
            "success": True,
            "data": DiseaseService.get_anxiety_prevalence()
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ============================================================
# Obesity
# ============================================================

@router.get(
    "/obesity",
    status_code=status.HTTP_200_OK
)
def get_obesity_prevalence():

    try:

        return {
            "success": True,
            "data": DiseaseService.get_obesity_prevalence()
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ============================================================
# Multi-Morbidity Analysis
# ============================================================

@router.get(
    "/comorbidity-analysis",
    status_code=status.HTTP_200_OK
)
def get_comorbidity_analysis():

    try:

        return {
            "success": True,
            "data": DiseaseService.get_comorbidity_analysis()
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

# ============================================================
# Chronic Disease Burden
# ============================================================

@router.get(
    "/chronic-disease-burden",
    status_code=status.HTTP_200_OK
)
def get_chronic_disease_burden():

    try:

        return {
            "success": True,
            "data": DiseaseService.get_chronic_disease_burden()
        }

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

@router.get("/dashboard-kpis")
def dashboard():

    image_stream = (
        DiseaseService.dashboard()
    )

    return StreamingResponse(
        image_stream,
        media_type="image/png"
    )