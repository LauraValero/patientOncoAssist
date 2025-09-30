import os
from typing import Optional

import httpx
from fastapi import HTTPException, status, Request, Security, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

http_bearer = HTTPBearer(auto_error=False)


def _get_auth_service_config() -> tuple[Optional[str], str]:
    base_url = os.getenv("AUTH_BASE_URL")
    print(f"base_url: {base_url}")
    validate_path = os.getenv("AUTH_VALIDATE_PATH", "/me")
    print(f"validate_path: {validate_path}")
    return base_url, validate_path


def _raise_unauthorized(detail: str) -> None:
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=detail)


def _raise_forbidden(detail: str) -> None:
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=detail)


def _validate_token_with_auth_service(token: str) -> dict:
    base_url, path = _get_auth_service_config()
    print(f"base_url_2: {base_url}")

    if not base_url:
        # Si no hay servicio de auth configurado, asumimos que el token es inválido
        _raise_forbidden("Invalid token")

    url = f"{base_url.rstrip('/')}{path}"
    try:
        with httpx.Client(timeout=10.0) as client:
            # La API de auth actual valida con GET /me y el header Authorization: Bearer <token>
            response = client.get(url, headers={"Authorization": f"Bearer {token}"})
    except httpx.TimeoutException:
        # Si el servicio de auth no responde, asumimos que el token es inválido
        _raise_forbidden("Invalid token")
    except httpx.RequestError as e:
        # Si no se puede conectar al servicio de auth, asumimos que el token es inválido
        _raise_forbidden("Invalid token")

    if response.status_code == 200:
        # Devolvemos la información del usuario autenticado como token_info
        data = response.json() if response.content else {}
        return data or {}
    elif response.status_code == 401:
        # El servicio de auth dice que el token es inválido, retornamos 403
        _raise_forbidden("Invalid token")
    elif response.status_code in (400, 403):
        _raise_forbidden("Invalid token")
    else:
        # Para otros errores, también asumimos token inválido
        _raise_forbidden("Invalid token")


def require_token(
    credentials: Optional[HTTPAuthorizationCredentials] = Depends(http_bearer),
    request: Request = None,
):
    if credentials is None:
        _raise_unauthorized("Authorization required")
    
    token = credentials.credentials
    if not token:
        _raise_unauthorized("Authorization required")
    
    token_info = _validate_token_with_auth_service(token)
    # Attach token info to request state for downstream use if needed
    if request is not None:
        setattr(request.state, "token_info", token_info)
    return token_info


