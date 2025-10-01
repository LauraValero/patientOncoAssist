import os

# Ruta del archivo .env
ENV_PATH = ".env"

# Cargar variables de entorno desde .env si existe
if os.path.exists(ENV_PATH):
    try:
        from dotenv import load_dotenv
        load_dotenv(ENV_PATH)
    except ImportError:
        # python-dotenv no está instalado, usar variables de entorno del sistema
        pass
    except Exception:
        # Error al cargar .env, continuar con variables de entorno del sistema
        pass

# Variables de entorno - funciona en local (.env) y en producción (variables del sistema)
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_SERVICE_ROLE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
AUTH_BASE_URL = os.getenv("AUTH_BASE_URL")
AUTH_VALIDATE_PATH = os.getenv("AUTH_VALIDATE_PATH", "/me")
