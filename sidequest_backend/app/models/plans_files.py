from datetime import datetime
from sqlalchemy import Column,String, Integer, ForeignKey, DateTime, UniqueConstraint
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.db.base import Base

class PlansFiles(Base):
    __tablename__ = "plans_files"

    id = Column(Integer, primary_key=True)
    plan_id = Column(Integer, ForeignKey("plans.id"), nullable=False)
    file_name = Column(String, nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    creada = Column(DateTime, default=datetime.utcnow)
    actualizada = Column(DateTime, nullable=True)
    eliminada = Column(DateTime, nullable=True)