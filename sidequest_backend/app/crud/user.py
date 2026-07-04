from datetime import datetime
import logging
import logging.config

from typing import List, Optional

from sqlalchemy.orm import Session
from sqlalchemy import desc

from app import models, schemas

from app.models.user import User
logging.config.fileConfig("/app/app/core/logging.conf")

def get_user_by_id(db: Session, user_id:int)-> User|None:
    return db.query(models.user.User).filter(models.user.User.id == user_id).first()

def get_user_by_email(db: Session, email:str)-> User|None:
    try:
        return db.query(models.user.User).filter(models.user.User.email == email).first()
    except Exception as e:
        logging.error(f"Error occurred while fetching user by email: {e}")
        return None


def create_user(db: Session, email: str, hashed_password:str, username:str)->User:
    user = User(email=email, hashed_password = hashed_password, username = username)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def set_role(db: Session, user: User, role:str)->User:
    user.role = role
    db.add(user)
    db.commit()
    db.refresh(user)
    return user