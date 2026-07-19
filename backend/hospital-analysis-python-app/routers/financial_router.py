from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from services.financial_service import (
    FinancialService
)

router = APIRouter(
    prefix="/financial",
    tags=["Financial Analytics"]
)


@router.get("/dashboard-kpis")
def dashboard():

    image_stream = (
        FinancialService
        .dashboard()
    )

    return StreamingResponse(
        image_stream,
        media_type="image/png"
    )