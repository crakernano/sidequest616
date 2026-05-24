from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.db.session import get_db

router = APIRouter()


@router.post("/", response_model=schemas.plan.Plan, status_code=201)
def create_plan(payload: schemas.plan.PlanCreate, db: Session = Depends(get_db)):
    return crud.plan.create_plan(db, payload)


@router.get("/", response_model=List[schemas.plan.Plan])
def list_plans(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.plan.get_plans(db, skip=skip, limit=limit)


@router.get("/{plan_id}", response_model=schemas.plan.Plan)
def retrieve_plan(plan_id: int, db: Session = Depends(get_db)):
    db_obj = crud.plan.get_plan(db, plan_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Plan not found")
    return db_obj


@router.put("/{plan_id}", response_model=schemas.plan.Plan)
def update_plan(plan_id: int, updates: schemas.plan.PlanUpdate, db: Session = Depends(get_db)):
    db_obj = crud.plan.get_plan(db, plan_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Plan not found")
    return crud.plan.update_plan(db, db_obj, updates)


@router.delete("/{plan_id}", status_code=204)
def delete_plan(plan_id: int, db: Session = Depends(get_db)):
    db_obj = crud.plan.get_plan(db, plan_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Plan not found")
    crud.plan.delete_plan(db, db_obj)
    return None
