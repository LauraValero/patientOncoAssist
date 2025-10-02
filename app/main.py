from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging
from app.routers import patient, clinical_history

app = FastAPI(
    title="Oncoassist Patients",
    description="API para gestión de pacientes oncológicos",
    version="1.0.0"
)

# Configurar CORS
origins = [
    "https://onco-care-ai.onrender.com",  # producción
    "http://localhost:3000",  # desarrollo local
    "http://127.0.0.1:3000",  # desarrollo local alternativo
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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
