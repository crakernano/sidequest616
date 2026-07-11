import logging
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.tag import TagBase, TagUpdate
from app.crud.tags import get_tags, create_tags, update_tag, assign_tag_to_plan
from app.db.session import get_db

from app.core.security import get_current_user

router = APIRouter()

@router.get("/", response_model=List[TagBase])
def list_plans(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_tags(db, skip=skip, limit=limit)

@router.post("/", response_model=TagBase, status_code=201)
def create_new_tag(payload: TagBase, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    try:
        return create_tags(db, payload)
    except Exception as e:
        logging.error(f"Error al crear el tag: {e}")
        raise HTTPException(status_code=400, detail="Error al crear el tag")
    
@router.put("/{tag_id}", response_model=TagBase)
def update_existing_tag(tag_id: int, payload: TagUpdate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    try:
        return update_tag(db, tag_id, payload)
    except Exception as e:
        logging.error(f"Error al actualizar el tag: {e}")
        raise HTTPException(status_code=400, detail="Error al actualizar el tag")
    
@router.patch("/{tag_id}/{plan_id}", response_model=TagBase)
def tag2plan(tag_id: int, plan_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    try:
        return assign_tag_to_plan(db, tag_id, plan_id)
    except Exception as e:
        logging.error(f"Error al asignar el tag al plan: {e}")
        raise HTTPException(status_code=400, detail="Error al asignar el tag al plan")