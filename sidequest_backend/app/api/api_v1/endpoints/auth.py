from fastapi import APIRouter, Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
import logging
from sqlalchemy.orm import Session

from app.core.security import create_access_token, get_current_user, oauth2_scheme, hash_password, verify_password, require_admin
from app.schemas.auth import Token, UserPublic, UserCreate,RoleUpdate
from app.db.session import get_db
from app.crud.user import get_user_by_email, create_user, get_user_by_id, set_role
from app.models.user import User

router = APIRouter()


@router.get("/secure")
def secure_endpoint(request: Request,token: str = Depends(oauth2_scheme)):
    return {"message": "acceso con token", "token recibido": token}

@router.post("/register", response_model=UserPublic, status_code=status.HTTP_201_CREATED)
def register_user(request: Request,payload: UserCreate, db:Session= Depends(get_db)):
    
    if get_user_by_email(db, payload.email) is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El correo ya está registrado")
    
    hashed_password = hash_password(payload.password)
    
    return create_user(db, email=payload.email, hashed_password=hashed_password, username=payload.username)
    
@router.post("/login", response_model=Token)
async def login(request: Request,form_data: OAuth2PasswordRequestForm = Depends(),db: Session = Depends(get_db)):
    
    user = get_user_by_email(db, email=form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales invalidas")
    try:
        token = create_access_token(sub=str(user.id))
        return Token(access_token=token, token_type="bearer", user=UserPublic.model_validate(user))
    except Exception as e:
        logging.error(f"Error occurred while creating access token: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al crear token")

@router.get("/me", response_model=UserPublic)
async def read_me(request: Request,current_user: User =Depends(get_current_user)):
    return UserPublic.model_validate(current_user)

@router.put("/role/{user_id}", response_model=UserPublic)
def update_role(request: Request,
            user_id: int, 
            db=Depends(get_db),
            payload: RoleUpdate = None,
            _admin: User = Depends(require_admin)):
    try:
        user = get_user_by_id(db, user_id)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
        updated_user = set_role(db, user, payload.role)
        return UserPublic.model_validate(updated_user)
    except Exception as e:
        logging.error(f"Error al actualizar el rol del usuario: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al actualizar el rol del usuario")