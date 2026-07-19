from fastapi import FastAPI

from routers.healthcare_router import router as healthcare_router


from routers.disease_router import (
    router as disease_router
)

from routers.risk_router import router as risk_router



from routers.clinical_risk_router import (
    router as clinical_risk_router
)

from routers.outcomes_router import (
    router as outcomes_router
)

from routers.financial_router import (
    router as financial_router
)

from routers.predictive_router import (
    router as predictive_router
)

from routers.executive_dashboard_router import (
    router as executive_router
)

from routers.population_router import(
    router as population_router
) 

from routers.readmission_router import (
    router as readmission_router
)

from routers.mortality_router import (
    router as mortality_router
)

from routers.icu_router import (
    router as icu_router
)

from routers.los_router import (
    router as los_router
)

from routers.cost_router import (
    router as cost_router
)

from routers.medication_router import (
    router as medication_router
)


app = FastAPI(
    title="Healthcare Analytics API",
    version="1.0"
)

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(medication_router)
app.include_router(cost_router)
app.include_router(los_router)
app.include_router(icu_router)
app.include_router(mortality_router)
app.include_router(readmission_router)
app.include_router(healthcare_router)
app.include_router(disease_router)
app.include_router(population_router)
app.include_router(clinical_risk_router)
app.include_router(outcomes_router)
app.include_router(financial_router)
app.include_router(predictive_router)
app.include_router(risk_router)
app.include_router(executive_router)

