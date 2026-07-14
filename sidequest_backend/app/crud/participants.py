import logging
from fastapi import FastAPI, Depends, HTTPException, status, APIRouter

from sqlalchemy.orm import Session
from app.models.plan_users import PlanUser

def get_plans(db: Session, skip: int = 0, limit: int = 100):
    """[DocString] - Devuelve todos los planes."""
    return db.query(PlanUser).offset(skip).limit(limit).all()

def get_participants_by_plan(db: Session, plan_id:int):
    """[DocString] - Devuelve todos los participantes de un plan."""
    try:
        return db.query(PlanUser).filter(PlanUser.plan_id == plan_id).all()
    except Exception as e:
        logging.error(f"Error occurred while fetching participants: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al obtener participantes")
    

def get_all_my_plans(db: Session, user_id:int):
    """[DocString] - Devuelve todos los planes de un usuario."""
    try:
        logging.info(f"Fetching plans for user_id: {user_id} - ")
        planes = db.query(PlanUser).filter(PlanUser.user_id == user_id).all()
        logging.info(f"Found {len(planes)} plans for user_id: {user_id}")
        return planes
    except Exception as e:
        logging.error(f"Error occurred while fetching my plans: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al obtener mis planes")