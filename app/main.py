from fastapi import FastAPI
from pathlib import Path
from dotenv import load_dotenv
import logging
from app.routers import patient, clinical_history

app = FastAPI(title="Oncoassist Patients")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app.include_router(patient.router)
app.include_router(clinical_history.router)


@app.on_event("startup")
async def startup_event():
    print("API started successfully")

@app.on_event("shutdown")
async def shutdown_event():
    print("API shutting down")
