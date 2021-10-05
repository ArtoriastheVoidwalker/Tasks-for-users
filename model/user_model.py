from sqlalchemy import (
    Column, String, DateTime
)
from base.db import Base
from fastapi_users.db import SQLAlchemyBaseUserTable


class User(Base, SQLAlchemyBaseUserTable):
    login = Column(String, unique=True)
    date = Column(DateTime)


users = User.__table__
