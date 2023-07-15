from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi_pagination import Page
from starlette import status

from src.dtos.example_dto import ExampleDto
from src.requests.example_request import ExampleRequest
from src.services.example_service import ExampleService

example_router = APIRouter()


@example_router.get('', tags=['Examples'], response_model=Page[ExampleDto], status_code=status.HTTP_201_CREATED)
async def index(service: Annotated[ExampleService, Depends(ExampleService)]):
    return service.find_all()


@example_router.post('', tags=['Examples'])
async def store(example_request: ExampleRequest,
                service: Annotated[ExampleService, Depends(ExampleService)]) -> ExampleDto:
    return service.store(example_request.model_dump())


@example_router.put('/{id}', tags=['Examples'])
async def update(id,
                 example_request: ExampleRequest,
                 service: Annotated[ExampleService, Depends(ExampleService)]) -> ExampleDto:
    return service.update(id, example_request.model_dump())


@example_router.delete('/{id}', tags=['Examples'], status_code=status.HTTP_204_NO_CONTENT)
async def destroy(id, service: Annotated[ExampleService, Depends(ExampleService)]) -> None:
    return service.delete(id)
