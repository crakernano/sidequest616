from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class PlanBase(BaseModel):
    title: str
    description: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None


class PlanCreate(PlanBase):
    pass


class PlanUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None


class PlanInDBBase(PlanBase):
    id: int
    created_at: Optional[datetime]

    class Config:
        orm_mode = True


class Plan(PlanInDBBase):
    pass
