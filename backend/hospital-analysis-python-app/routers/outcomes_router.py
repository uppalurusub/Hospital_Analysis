from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from services.outcomes_service import (
    OutcomesService
)

router = APIRouter(
    prefix="/outcomes",
    tags=["Outcomes Analytics"]
)


@router.get("/dashboard-kpis")
def dashboard():

    image_stream = (
        OutcomesService
        .dashboard()
    )

    return StreamingResponse(
        image_stream,
        media_type="image/png"
    )