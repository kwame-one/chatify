from app.controllers.example_controller import example_router


def register_routes(app):
    app.include_router(example_router, prefix='/examples')
