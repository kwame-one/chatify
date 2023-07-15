from fastapi import FastAPI
from fastapi_pagination import add_pagination

from src.controllers import register_routes
from src.exceptions import register_exception_handlers
from src.middlewares import register_middlewares

app = FastAPI()

register_exception_handlers(app)
register_middlewares(app)

register_routes(app)

add_pagination(app)

