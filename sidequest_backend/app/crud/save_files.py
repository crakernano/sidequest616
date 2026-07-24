from datetime import datetime
import logging
import logging.config

from typing import List, Optional

from sqlalchemy.orm import Session
from sqlalchemy import desc

from app import models, schemas

def save_file(db: Session, plan_id: int, file: str, owner_id: int):
    try:
        logging.info(f"Asociando el fichero {file} al plan {plan_id}")
        db_obj = models.PlansFiles(plan_id=plan_id, file_name=file, owner_id=owner_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    except Exception as e:
        logging.error(f"Error al asociar el fichero {file} al plan {plan_id}: {str(e)}")
        db.rollback()
        raise e

def get_files_for_plan(db: Session,plan_id: int):
    return db.query(models.PlansFiles).filter(models.PlansFiles.plan_id == plan_id).all()