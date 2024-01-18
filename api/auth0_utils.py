from typing import Optional 

import jwt 
from fastapi import Depends, HTTPException, status 
from fastapi.security import SecurityScopes, HTTPAuthorizationCredentials, HTTPBearer 
from .auth0_config import get_settings 

class UnauthorizedException(HTTPException):
    def __init__(self, detail: str, **kwargs):
        
# """Returns HTTP 403"""
        super().__init__(status.HTTP_403_FORBIDDEN, detail=detail)

class UnauthenticatedException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Requires authentication"
        )


class VerifyToken:
    """Does all the token verification using PyJWT"""

    def __init__(self):
        self.config = get_settings()

        # This gets the JWKS from a given URL and does processing so you can
        # use any of the keys available
        jwks_url = f'https://{self.config.auth0_domain}/.well-known/jwks.json'
        self.jwks_client = jwt.PyJWKClient(jwks_url)

   
    async def verify(self, security_scopes: SecurityScopes, token: Optional[HTTPAuthorizationCredentials] = Depends(HTTPBearer())):
        if token is None:
            raise UnauthenticatedException

        # Imprime el token recibido para depuración
        print("Token recibido:", token.credentials)

        # Intenta obtener la clave de firma pública
        try:
            signing_key = self.jwks_client.get_signing_key_from_jwt(token.credentials).key
            print("Clave de firma pública obtenida:", signing_key)
        except jwt.exceptions.PyJWKClientError as error:
            print("Error obteniendo la clave de firma:", error)
            raise UnauthorizedException(str(error))
        except jwt.exceptions.DecodeError as error:
            print("Error de decodificación al obtener la clave de firma:", error)
            raise UnauthorizedException(str(error))

        # Intenta decodificar el payload del token
        try:
            payload = jwt.decode(
                token.credentials,
                signing_key,
                algorithms=self.config.auth0_algorithms,
                audience=self.config.auth0_api_audience,
                issuer=self.config.auth0_issuer,
            )
            print("Payload decodificado:", payload)
        except jwt.ExpiredSignatureError as error:
            print("Token expirado:", error)
            raise UnauthorizedException("Token expirado")
        except jwt.JWTClaimsError as error:
            print("Error en las claims del token:", error)
            raise UnauthorizedException("Error en las claims del token")
        except Exception as error:
            print("Error general durante la decodificación del token:", error)
            raise UnauthorizedException(str(error))
        
        return payload

  