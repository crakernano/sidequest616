from typing import Optional, List
from pydantic import BaseModel,ConfigDict
from datetime import datetime
from app.schemas.auth import UserPublic

class PlanBase(BaseModel):
    title: str
    description: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None


class PlanCreate(PlanBase):
    title: str
    description: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None


class PlanUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None


class PlanInDBBase(PlanBase):
    id: int
    created_at: Optional[datetime]

    class Config:
        #orm_mode = True
        model_config = ConfigDict(from_attributes=True)


class Plan(PlanInDBBase):
    pass

class PlanResponse(PlanBase):
    id: int
    participants: List[UserPublic] = []

class AddParticipantSchema(BaseModel):
    user_id: int
    plan_id: int