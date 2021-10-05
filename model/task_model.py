from base.db import Base
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column, String, Integer, DateTime, ForeignKey, Boolean, sql
)


class Task(Base):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String)
    text = Column(String(355))
    date = Column(DateTime, server_default=sql.func.now())
    is_completed = Column(Boolean, default=False)
    is_important = Column(Boolean, default=False)
    user = Column(String, ForeignKey('user.id'))
    user_id = relationship("User")


tasks = Task.__table__
