from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from services.executive_dashboard_service import (
    ExecutiveDashboardService
)

router = APIRouter(
    prefix="/executive",
    tags=["Executive Dashboard"]
)


@router.get("/dashboard-kpis")
def dashboard():

    image_stream = (
        ExecutiveDashboardService
        .dashboard()
    )

    return StreamingResponse(
        image_stream,
        media_type="image/png"
    )