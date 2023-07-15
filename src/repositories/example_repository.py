from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from src.models.example import Example
from src.repositories.base_repository import BaseRepository
from configs.database import get_db


class ExampleRepository(BaseRepository):
    def __init__(self, db_session: Annotated[Session, Depends(get_db)]):
        super().__init__(model=Example, db_session=db_session)
