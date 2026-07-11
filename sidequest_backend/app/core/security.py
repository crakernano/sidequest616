from os import getenv
import logging
from datetime import timedelta,datetime,timezone
from typing import Optional, Literal
from fastapi import Depends
import jwt
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError, PyJWTError
from sqlalchemy.orm import Session
from pwdlib import PasswordHash


from fastapi.security import OAuth2PasswordBearer
from app.core.exceptions import raise_expired_token, raise_credentials_exc, raise_forbidden_exc
from app.db.session import get_db
from app.models.user import User

#ToDo: Traer esta informacion del settings 
SECRET_KEY = getenv("SECRET_KEY","mysecretkey")
ALGORITHM = getenv("ALGORITHM","HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

password_hash =PasswordHash.recommended()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

# def create_access_token(data: dict,expires_delta:Optional[timedelta]=None):
#     to_encode = data.copy()
#     expire = datetime.now(tz=timezone.utc) + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
#     to_encode.update({"exp":expire})
#     token = jwt.encode(payload=to_encode, key=SECRET_KEY, algorithm=ALGORITHM)
#     return token


def create_access_token(sub:str, minutes:int | None= None)->str:
    expire = datetime.now(tz=timezone.utc) + timedelta(minutes=minutes or ACCESS_TOKEN_EXPIRE_MINUTES)
    token = jwt.encode(payload={"sub":sub, "exp":expire}, key=SECRET_KEY, algorithm=ALGORITHM)
    return token

def decode_token(token:str) -> dict:
    payload = jwt.decode(jwt=token, key=SECRET_KEY, algorithms=[ALGORITHM])
    return payload
    
async def get_current_user(db: Session= Depends(get_db),  token:str = Depends(oauth2_scheme))->User:
    try:
        payload = decode_token(token)
        #logging.info("Decodificando token: %s", payload)
        sub: Optional[str] = payload.get("sub")
        if not sub:
            logging.error("Token válido pero falta el campo 'sub' en el payload: %s", payload)
            raise raise_credentials_exc()
        
        user_id = int(sub)
        #logging.debug("Usuario extraído del token: %s (token prefix: %s)", user_id, token[:10])
    
    except ExpiredSignatureError as exc:
        logging.warning("Token expirado: prefix=%s, error=%s", token[:10], exc)
        raise raise_expired_token()
    
    except InvalidTokenError as exc:
        logging.warning("Token inválido: prefix=%s, error=%s", token[:10], exc)
        raise raise_credentials_exc()
    
    except PyJWTError as exc:
        logging.error("Error JWT al decodificar token: prefix=%s, error=%s", token[:10], exc)
        raise raise_credentials_exc()
    
    user = db.get(User, user_id)
    if not user:
        logging.warning("Usuario no encontrado para user_id=%s, token prefix=%s", user_id, token[:10])
        raise raise_credentials_exc()
    if not user.is_active:
        logging.warning("Usuario no activo user_id=%s, token prefix=%s", user_id, token[:10])
        raise raise_credentials_exc()
    
    #logging.info("Usuario autenticado correctamente: user_id=%s", user_id)
    return user

def hash_password(password:str)->str:
    return password_hash.hash(password)

def verify_password(plain_password:str, hashed_password:str)->bool:
    return password_hash.verify(plain_password, hashed_password)

def require_role(min_role: Literal["user", "moderator","admin"]):
    order = {"user":0, "moderator":1, "admin":2}

    def evaluator(user: User = Depends(get_current_user))->User:
        if order[user.role] <order[min_role]:
            raise raise_forbidden_exc()

    return evaluator

require_user = require_role("user")
require_moderator = require_role("moderator")
require_admin = require_role("admin")