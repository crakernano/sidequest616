from sqlalchemy import Column, Integer, ForeignKey, DateTime, UniqueConstraint
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.db.base import Base


class PlanTag(Base):
    __tablename__ = "plan_tags"

    id = Column(Integer, primary_key=True)
    plan_id = Column(Integer, ForeignKey("plans.id"), nullable=False)
    tag_id = Column(Integer, ForeignKey("tags.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    plan = relationship("Plan", back_populates="plan_tags")
    tag = relationship("Tags", back_populates="plan_tags")

    __table_args__ = (UniqueConstraint("plan_id", "tag_id", name="uix_plan_tag"),)
