from abc import ABC
from typing import Annotated

from fastapi import Depends

from src.dtos.example_dto import ExampleDto
from src.repositories.example_repository import ExampleRepository
from src.services.base_service import BaseService


class ExampleService(BaseService, ABC):

    def __init__(self, example_repo: Annotated[ExampleRepository, Depends(ExampleRepository)]):
        super().__init__(repository=example_repo)

    def get_dto(self):
        return ExampleDto
