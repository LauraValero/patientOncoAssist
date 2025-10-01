# OncoAssist - Sistema de Gestión de Pacientes Oncológicos

Sistema de gestión para pacientes oncológicos con historias clínicas y recomendaciones de tratamiento basadas en IA.

## Características

- **Gestión de Pacientes**: CRUD completo para información demográfica de pacientes
- **Historias Clínicas**: Registro detallado de información médica y clínica
- **Recomendaciones IA**: Sistema de recomendaciones de tratamiento automatizado
- **API REST**: Endpoints bien documentados con FastAPI
- **Autenticación**: Sistema de autenticación con tokens JWT
- **Base de Datos**: Integración con Supabase/PostgreSQL

## Tecnologías

- **Backend**: FastAPI, Python 3.8+
- **Base de Datos**: PostgreSQL (Supabase)
- **Autenticación**: JWT tokens
- **Documentación**: Swagger UI automática

## Requisitos

- Python 3.8+
- PostgreSQL (o cuenta de Supabase)
- Git

## Instalación

### Desarrollo Local

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/LauraValero/patientOncoAssist.git
   cd patientOncoAssist
   ```

2. **Crear entorno virtual**:
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar variables de entorno**:
   Crear archivo `.env` en la raíz del proyecto:
   ```env
   SUPABASE_URL=tu_url_de_supabase
   SUPABASE_SERVICE_ROLE_KEY=tu_service_role_key
   AUTH_BASE_URL=https://tu-auth-service.com
   AUTH_VALIDATE_PATH=/me
   ENVIRONMENT=development
   DEBUG=True
   ```

5. **Ejecutar la aplicación**:
   ```bash
   cd app
   python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

## API Documentation

Una vez ejecutada la aplicación, puedes acceder a:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Base de Datos

El esquema de la base de datos se encuentra en `app/sql/create_tables.sql`. Ejecuta este script en tu base de datos supabase.

## Estructura del Proyecto

```
OncoAssist/
├── app/
│   ├── core/           # Configuración core (DB, seguridad)
│   ├── models/         # Modelos de datos
│   ├── routers/        # Endpoints de la API
│   ├── schemas/        # Esquemas Pydantic
│   ├── services/       # Lógica de negocio
│   ├── sql/           # Scripts SQL
│   └── main.py        # Aplicación principal
├── requirements.txt   # Dependencias Python
└── README.md         # Este archivo
```

## 🔐 Autenticación

El sistema utiliza autenticación basada en tokens JWT. Incluye el header:
```
Authorization: Bearer <tu_token>
```

## Modelos de Datos

### Paciente
- Información demográfica básica
- Datos de contacto
- Información geográfica

### Historia Clínica
- Antecedentes familiares y personales
- Información del diagnóstico
- Factores de estilo de vida
- Tratamientos recibidos
- Seguimiento y adherencia
