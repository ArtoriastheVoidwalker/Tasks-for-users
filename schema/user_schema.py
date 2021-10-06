import uuid
import pydantic
from fastapi_users import models
from pydantic import EmailStr, BaseModel
from typing import Optional


class User(models.BaseUser):
    class Config:
        orm_mode = True


class UserInTask(BaseModel):
    id: Optional[str]
    name: str = None

    @pydantic.validator("id", pre=True, always=True)
    def default_id(cls, v):
        return v or str(uuid.uuid4())

    class Config:
        orm_mode = True


class UserCreate(models.BaseUserCreate):
    name: str


class UserUpdate(models.BaseUserUpdate):
    pass


class UserDB(User, models.BaseUserDB):
    pass
