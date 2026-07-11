from typing import Optional
from pydantic import BaseModel,ConfigDict, validator
from datetime import datetime


class TagBase(BaseModel):
    tag: str
    color: Optional[str] = None
    
    @validator("color")
    def validate_color(cls, value):
        if len(value) != 7 or not value.startswith("#"):
            raise ValueError("El color debe tener formato #xxxxxx")
        if any(c not in "0123456789abcdefABCDEF" for c in value[1:]):
            raise ValueError("El color debe contener solo hexadecimales")
        return value

class TagUpdate(BaseModel):
    tag: str
    color: Optional[str] = None
    enable: Optional[bool] = True

class TagCreate(TagBase):
    owner_id: Optional[int] = None
    model_config = ConfigDict(from_attributes=True)