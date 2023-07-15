from starlette.middleware.cors import CORSMiddleware


def register_middlewares(app):
    app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"],
                       allow_headers=["*"])