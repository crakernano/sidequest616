from fastapi import FastAPI
from app.api.api_v1.api import api_router


def create_app() -> FastAPI:
    app = FastAPI(title="Plans API")
    app.include_router(api_router, prefix="/api/v1")
    return app


app = create_app()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
