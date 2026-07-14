from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.db.base import Base
from app.models.plan_users import PlanUser

class Plan(Base):
    __tablename__ = "plans"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False, index=True)
    description = Column(Text, nullable=True)
    start_date = Column(String(50), nullable=True)
    end_date = Column(String(50), nullable=True)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    url = Column(String(255), nullable=True)
    location = Column(String(255), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    plan_tags = relationship("PlanTag", back_populates="plan", cascade="all, delete-orphan")
    participants = relationship("User", secondary=PlanUser.__table__, back_populates="plans")
# Importar PlanTag al final para evitar circular imports
from app.models.plan_tags import PlanTag  # noqa: E402, F401
