import logging
from supabase import create_client, Client
from .config import SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Validar que las variables estén configuradas
if not SUPABASE_URL or not SUPABASE_SERVICE_ROLE_KEY:
    raise RuntimeError(
        "Faltan variables de entorno SUPABASE_URL o SUPABASE_SERVICE_ROLE_KEY"
    )

try:
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY)
    logger.info("Conexión a Supabase establecida correctamente")
except Exception as e:
    logger.error(f"Error al conectar con Supabase: {e}")
    raise RuntimeError(f"No se pudo conectar con Supabase: {e}")
