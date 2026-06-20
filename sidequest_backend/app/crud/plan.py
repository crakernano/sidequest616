"""[DocString] - Interacción con la base de datos para lógica de negocio."""

# pylint: disable=superfluous-parens, too-many-arguments
from datetime import datetime
import logging
import logging.config

from typing import List, Optional

from sqlalchemy.orm import Session
from sqlalchemy import desc

from app import models, schemas

from app.models.plan import Plan
logging.config.fileConfig("/app/app/core/logging.conf")

def get_plans(db: Session, skip: int = 0, limit: int = 100):
    """[DocString] - Devuelve todos los planes."""
    return db.query(Plan).offset(skip).limit(limit).all()

def create_plan(db: Session, plan_in: schemas.plan.PlanCreate) -> models.plan.Plan:
    logging.info(f"Creando plan: {plan_in.title}")
    db_obj = models.plan.Plan(**plan_in.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_plan(db: Session, plan_id: int) -> Optional[models.plan.Plan]:
    return db.query(models.plan.Plan).filter(models.plan.Plan.id == plan_id).first()

def update_plan(db: Session, db_obj: models.plan.Plan, updates: schemas.plan.PlanUpdate) -> models.plan.Plan:
    for field, value in updates.dict(exclude_unset=True).items():
        setattr(db_obj, field, value)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_plan(db: Session, db_obj: models.plan.Plan) -> None:
    pass
# from sqlalchemy.orm import Session
# from typing import List, Optional
# from app import models, schemas


# def get_plan(db: Session, plan_id: int) -> Optional[models.plan.Plan]:
#     return db.query(models.plan.Plan).filter(models.plan.Plan.id == plan_id).first()


# def get_plans(db: Session, skip: int = 0, limit: int = 100) -> List[models.plan.Plan]:
#     return db.query(models.plan.Plan).offset(skip).limit(limit).all()


# def create_plan(db: Session, plan_in: schemas.plan.PlanCreate) -> models.plan.Plan:
#     db_obj = models.plan.Plan(**plan_in.dict())
#     db.add(db_obj)
#     db.commit()
#     db.refresh(db_obj)
#     return db_obj


# def update_plan(db: Session, db_obj: models.plan.Plan, updates: schemas.plan.PlanUpdate) -> models.plan.Plan:
#     for field, value in updates.dict(exclude_unset=True).items():
#         setattr(db_obj, field, value)
#     db.add(db_obj)
#     db.commit()
#     db.refresh(db_obj)
#     return db_obj


# def delete_plan(db: Session, db_obj: models.plan.Plan) -> None:
#     db.delete(db_obj)
#     db.commit()
