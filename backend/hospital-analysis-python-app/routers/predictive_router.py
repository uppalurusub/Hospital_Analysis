from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from services.predictive_service import (
    PredictiveService
)

router = APIRouter(
    prefix="/predictive",
    tags=["Predictive Analytics"]
)


@router.get("/dashboard-kpis")
def dashboard():

    image_stream = (
        PredictiveService
        .dashboard()
    )

    return StreamingResponse(
        image_stream,
        media_type="image/png"
    )