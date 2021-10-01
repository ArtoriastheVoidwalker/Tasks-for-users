from typing import Optional

from pydantic import BaseModel
from datetime import datetime
from user.model_pyndantic import User


class TaskBase(BaseModel):
    title: str
    text: str
    is_important: bool
    user: str
    # user: Optional[User] = None


class TitleList(TaskBase):
    id: int
    date: datetime


class TaskCreate(TaskBase):
    class Config:
        orm_mode = True
