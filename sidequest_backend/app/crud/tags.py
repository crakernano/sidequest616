from datetime import datetime
import logging
import logging.config

from typing import List, Optional

from sqlalchemy.orm import Session
from sqlalchemy import desc

from app import models, schemas

from app.models.tags import Tags
from app.models.plan_tags import PlanTag

def get_tags(db: Session, skip: int = 0, limit: int = 100):
    """[DocString] - Devuelve todos los planes."""
    return db.query(Tags).offset(skip).limit(limit).all()

def create_tags(db: Session, tag_in: schemas.tag.TagBase) -> models.tags.Tags:
    logging.info(f"Creando el tag: {tag_in.tag}")
    db_obj = models.tags.Tags(**tag_in.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_tag(db: Session, tag_id: int, tag_in: schemas.tag.TagUpdate) -> models.tags.Tags:
    tag = db.query(Tags).filter(Tags.id == tag_id).first()
    if not tag:
        raise ValueError(f"Tag with id {tag_id} not found")
    
    for key, value in tag_in.dict(exclude_unset=True).items():
        setattr(tag, key, value)
    
    db.commit()
    db.refresh(tag)
    return tag

def assign_tag_to_plan(db: Session, tag_id: int, plan_id: int) -> models.tags.Tags:
    tag = db.query(Tags).filter(Tags.id == tag_id).first()
    if not tag:
        raise ValueError(f"Tag with id {tag_id} not found")
    
    plan = db.query(models.plan.Plan).filter(models.plan.Plan.id == plan_id).first()
    if not plan:
        raise ValueError(f"Plan with id {plan_id} not found")

    plan_tag = PlanTag(plan_id=plan_id, tag_id=tag_id)
    db.add(plan_tag)
    db.commit()
    db.refresh(tag)
    return tag

def get_tags_by_plan(db: Session, plan_id: int) -> List[models.tags.Tags]:
    plan_tags = db.query(PlanTag).filter(PlanTag.plan_id == plan_id).all()
    tag_ids = [pt.tag_id for pt in plan_tags]
    return db.query(Tags).filter(Tags.id.in_(tag_ids)).all()