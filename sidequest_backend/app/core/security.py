from os import getenv
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
    
async def get_current_user(db: Session= Depends(get_db),  token:str = Depends(oauth2_scheme)):
    try:
        payload = decode_token(token)
        sub: Optional[str] =payload.get("sub")
        username : Optional[str] = payload.get("username")
        if sub is None or username is None:
            raise raise_credentials_exc()
        
        user_id =int(sub)
        #return {"email":sub, "username":username}
    
    except ExpiredSignatureError:
        raise raise_expired_token()
    
    except InvalidTokenError:
        raise raise_credentials_exc()
    
    except  PyJWTError:
        raise raise_credentials_exc()
    
    user = db.get(User, user_id)

    if not user or not user.is_active:
        raise raise_credentials_exc()
    
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