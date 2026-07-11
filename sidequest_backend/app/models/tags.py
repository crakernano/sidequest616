
from datetime import datetime
from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
    DateTime,
    TIMESTAMP,
    Text,
    Float,
    JSON,
    PrimaryKeyConstraint,
)

from sqlalchemy.sql import func

from app.db.base import Base
from sqlalchemy.orm import relationship

class Tags(Base):
    """[DocString] - Etiquetas para categorizar planes."""

    __tablename__ = "tags"
    id = Column(Integer, primary_key=True)
    tag = Column(String(256), unique=True, nullable=False)
    plan_tags = relationship("PlanTag", back_populates="tag", cascade="all, delete-orphan")
    color = Column(String(256), nullable=True, default="#FFFFFF")
    user_owner_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    enable = Column(Boolean, nullable=True, default=True)
    creada = Column(DateTime, default=datetime.utcnow)
    actualizada = Column(DateTime, nullable=True)
    eliminada = Column(DateTime, nullable=True)

