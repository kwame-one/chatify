from fastapi import FastAPI
from fastapi_pagination import add_pagination

from app.controllers import register_routes
from app.exceptions import register_exception_handlers
from app.middlewares import register_middlewares

app = FastAPI()

register_exception_handlers(app)
register_middlewares(app)

register_routes(app)

add_pagination(app)

