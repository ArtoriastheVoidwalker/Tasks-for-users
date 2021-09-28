from core.db import Base
from user.models import User
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column, String, Integer, DateTime, ForeignKey, Boolean
)


class Task(Base):
    __tablename__ = "users_tasks"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String)
    text = Column(String(255))
    date = Column(DateTime)
    is_completed = Column(Boolean, default=False)
    user = Column(Integer, ForeignKey("user.id"))
    user_id = relationship(User)
