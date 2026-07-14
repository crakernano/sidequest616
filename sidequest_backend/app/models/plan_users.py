from sqlalchemy import Column, ForeignKey, Integer
from app.db.base import Base

# Tabla intermedia para la relación Muchos a Muchos
class PlanUser(Base):
    __tablename__ = "plan_participants"

    user_id = Column("user_id", Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    plan_id = Column("plan_id", Integer, ForeignKey("plans.id", ondelete="CASCADE"), primary_key=True)