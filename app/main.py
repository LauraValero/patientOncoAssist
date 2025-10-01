from fastapi import FastAPI
import logging
from app.routers import patient, clinical_history

app = FastAPI(
    title="Oncoassist Patients",
    description="API para gestión de pacientes oncológicos",
    version="1.0.0"
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Incluir routers
app.include_router(patient.router)
app.include_router(clinical_history.router)

@app.get("/")
async def root():
    return {"message": "Oncoassist API is running", "status": "ok"}


@app.on_event("startup")
async def startup_event():
    print("API started successfully")

@app.on_event("shutdown")
async def shutdown_event():
    print("API shutting down")
