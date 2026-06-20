from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud
from app.db.session import get_db
from app.schemas.plan import Plan, PlanCreate, PlanUpdate
from app.crud.plan import create_plan, get_plan, get_plans, update_plan, delete_plan
router = APIRouter()


@router.post("/", response_model=Plan, status_code=201)
def create_new_plan(payload: PlanCreate, db: Session = Depends(get_db)):
    return create_plan(db, payload)


@router.get("/", response_model=List[Plan])
def list_plans(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_plans(db, skip=skip, limit=limit)


@router.get("/{plan_id}", response_model=Plan)
def retrieve_plan(plan_id: int, db: Session = Depends(get_db)):
    db_obj = get_plan(db, plan_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Plan not found")
    return db_obj


@router.put("/{plan_id}", response_model=Plan)
def edit_plan(plan_id: int, updates: PlanUpdate, db: Session = Depends(get_db)):
    db_obj = get_plan(db, plan_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Plan not found")
    return update_plan(db, db_obj, updates)


@router.delete("/{plan_id}", status_code=204)
def remove_plan(plan_id: int, db: Session = Depends(get_db)):
    db_obj = get_plan(db, plan_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Plan not found")
    delete_plan(db, db_obj)
    return {"message": f"Plan {plan_id} deleted successfully"}
