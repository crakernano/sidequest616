from typing import Optional
from pydantic import BaseModel,ConfigDict
from datetime import datetime


class FilePlan(BaseModel):
    plan_id: int
    file_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)