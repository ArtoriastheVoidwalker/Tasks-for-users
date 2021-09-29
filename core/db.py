from sqlalchemy import create_engine
import databases
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta

from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
SQLALCHEMY_DATABASE_URL = "postgresql://junback:junback@localhost/junback"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
database = databases.Database(SQLALCHEMY_DATABASE_URL)
Base: DeclarativeMeta = declarative_base()

