from fastapi import FastAPI
from routes.no_show import router as no_show_router
from routes.triage import router as triage_router
from routes.risk import router as risk_router
app = FastAPI(title="OrtemHealth ML APIs", version="1.0")
app.include_router(no_show_router)
app.include_router(triage_router)
app.include_router(risk_router)
