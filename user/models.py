from sqlalchemy import (
    Column, String, Integer, DateTime, Boolean
)
from core.db import Base
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase


class User(Base, SQLAlchemyBaseUserTable):
    login = Column(String, unique=True)
    date = Column(DateTime)


users = User.__table__

# class User(Base):
#     __tablename__ = "user"
#     id = Column(Integer, primary_key=True, index=True, unique=True)
#     # При создании нового пользователя должен обрабатываться его «login» (на предмет его уникальности).
#     login = Column(String, unique=True)
#     password = Column(String)
#     date = Column(DateTime)
#     # Ввести тип пользователя — admin, который может просматривать задачи всех пользователей
#     is_admin = Column(Boolean, default=False)
