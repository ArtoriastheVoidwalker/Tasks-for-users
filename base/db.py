import databases
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import (
    declarative_base, DeclarativeMeta
)

SQLALCHEMY_DATABASE_URL = "postgresql://junback:junback@localhost/junback"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

database = databases.Database(SQLALCHEMY_DATABASE_URL)
Base: DeclarativeMeta = declarative_base()
