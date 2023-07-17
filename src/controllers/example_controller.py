from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi_pagination import Page
from starlette import status

from src.dtos.example_dto import ExampleDto
from src.requests.example_request import ExampleRequest
from src.services.example_service import ExampleService

example_router = APIRouter(tags=['Examples'])


@example_router.get('', response_model=Page[ExampleDto], status_code=status.HTTP_201_CREATED)
async def index(service: Annotated[ExampleService, Depends(ExampleService)]):
    return service.find_all()


@example_router.get('/{id}')
async def find(id, service: Annotated[ExampleService, Depends(ExampleService)]):
    return service.find(id)


@example_router.post('')
async def store(example_request: ExampleRequest,
                service: Annotated[ExampleService, Depends(ExampleService)]) -> ExampleDto:
    return service.store(example_request.model_dump())


@example_router.put('/{id}')
async def update(id,
                 example_request: ExampleRequest,
                 service: Annotated[ExampleService, Depends(ExampleService)]) -> ExampleDto:
    return service.update(id, example_request.model_dump())


@example_router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy(id, service: Annotated[ExampleService, Depends(ExampleService)]) -> None:
    return service.delete(id)
