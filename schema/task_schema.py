from pydantic import BaseModel
from datetime import datetime
from .user_schema import UserInTask


class TaskBase(BaseModel):
    title: str
    text: str
    is_important: bool


class TitleList(TaskBase):
    id: int
    date: datetime
    user: UserInTask


class TaskCreate(TaskBase):
    class Config:
        orm_mode = True


class TaskSingle(TitleList):
    pass
