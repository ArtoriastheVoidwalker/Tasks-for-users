from pydantic import BaseModel
from datetime import datetime


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
