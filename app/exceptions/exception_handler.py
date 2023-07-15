from starlette.requests import Request
from starlette.responses import JSONResponse
from fastapi import status

from app.exceptions.resource_not_found_exception import ResourceNotFoundException


def resource_not_found_exception_handler(request: Request, exception: ResourceNotFoundException):
    return JSONResponse(content={'message': exception.description}, status_code=status.HTTP_404_NOT_FOUND)
