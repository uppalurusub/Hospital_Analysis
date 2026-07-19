from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from services.clinical_risk_service import (
    ClinicalRiskService
)

router = APIRouter(
    prefix="/clinical-risk",
    tags=["Clinical Risk Analytics"]
)

service = ClinicalRiskService()


@router.get("/dashboard-kpis")
def dashboard():

    image_stream = (
        ClinicalRiskService
        .dashboard()
    )

    return StreamingResponse(
        image_stream,
        media_type="image/png"
    )