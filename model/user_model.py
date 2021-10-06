from sqlalchemy import (
    Column, String, DateTime
)
from base.db import Base
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase


class User(Base, SQLAlchemyBaseUserTable):
    name = Column(String, unique=True)
    date = Column(DateTime)


users = User.__table__
