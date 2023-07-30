from fastapi import FastAPI
from src.router import router


def create_app() -> FastAPI:
    app: FastAPI = FastAPI()
    app.include_router(router=router)

    return app
