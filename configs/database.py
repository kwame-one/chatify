from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .app import settings

engine = create_engine(
    f"postgresql://{settings.database_user}:{settings.database_password}@{settings.database_host}:{settings.database_port}/{settings.database_name}")

DbSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = DbSession()
    try:
        yield db
    finally:
        db.close()
