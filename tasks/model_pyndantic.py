from pydantic import BaseModel
from datetime import datetime


class TaskBase(BaseModel):
    title: str
    text: str
    date: datetime

    class Config:
        orm_mode = True


class TitleList(TaskBase):
    id: int


class TaskCreate(TaskBase):
    pass
