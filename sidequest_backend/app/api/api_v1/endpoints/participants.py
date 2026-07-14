import logging
from fastapi import FastAPI, Depends, HTTPException, status, APIRouter
from sqlalchemy.orm import Session
from app.schemas.plan import Plan
from app.models.user import User
from app.db.session import get_db
from app.schemas.plan import PlanResponse, AddParticipantSchema
from app.crud.participants import get_participants_by_plan, get_all_my_plans
from app.crud.plan import get_plan
from app.core.security import get_current_user

router = APIRouter()


@router.get("/plans/{id}/participants", tags=["participants"])
def get_participants(id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    try:
        return get_participants_by_plan(db, plan_id=id)
    except Exception as e:
        logging.error(f"Error occurred while fetching participants: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al obtener participantes")

#ToDo: Crear un BackgroundTasks para notificar que ha sido invitado
@router.post("/plans/{plan_id}/participants", response_model=PlanResponse, status_code=status.HTTP_200_OK)
def add_participant_to_plan(plan_id: int, payload: AddParticipantSchema, db: Session = Depends(get_db)):
    plan = db.query(Plan).filter(Plan.id == plan_id).first()
    if not plan:
        raise HTTPException(status_code=404, detail="Plan no encontrado")
        
    user = db.query(User).filter(User.id == payload.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    if user in plan.participants:
        raise HTTPException(status_code=400, detail="El usuario ya está unido a este plan")

    plan.participants.append(user)
    db.commit()
    db.refresh(plan)
    return plan

@router.delete("/plans/{plan_id}/participants/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_participant_from_plan(plan_id: int, user_id: int, db: Session = Depends(get_db)):
    pass

@router.get("/my-plans", status_code=status.HTTP_200_OK)
def get_my_plans(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    #logging.info(f"Current user: {current_user.username}, ID: {current_user.id}")
    plans = []

    user_plans = get_all_my_plans(db, user_id=current_user.id)

    for plan_user in user_plans:
        plan = get_plan(db, plan_id=plan_user.plan_id)
        plans.append(plan)
    return plans
