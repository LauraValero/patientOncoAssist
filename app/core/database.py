import os
import logging
from pathlib import Path
from dotenv import load_dotenv
from supabase import create_client, Client

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env"

if not ENV_PATH.exists():
    raise RuntimeError(f"No se encontro el archivo .env en {ENV_PATH}")

load_dotenv(dotenv_path=ENV_PATH)

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_SERVICE_ROLE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

if not SUPABASE_URL or not SUPABASE_SERVICE_ROLE_KEY:
    raise RuntimeError("Faltan credenciales de Supabase en el archivo .env")

try:
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY)
    logger.info("Conexión a Supabase establecida correctamente")
except Exception as e:
    logger.error(f"Error al conectar con Supabase: {e}")
    raise RuntimeError(f"No se pudo conectar con Supabase: {e}")
