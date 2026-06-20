from fastapi import FastAPI
from fastapi_prometheus_exporter import PrometheusExporterMiddleware

#import logging
#import logging.config
from app.db.session import engine
from app.models import plan as models
from app.api.api_v1.api import api_router


def create_app() -> FastAPI:
    app = FastAPI(title="Plans API")
    app.include_router(api_router, prefix="/api/v1")
    return app

app = create_app()

models.Base.metadata.create_all(bind=engine)

#logging.config.fileConfig("./app/core/logging.conf")
PrometheusExporterMiddleware.setup(
    app=app,
    metrics_path="/metrics",
    ignore_paths=["/healthz", "/metrics"],
)


if __name__ == "__main__":
    import uvicorn
    #logging.info("Arrancando SideQuest Backend")
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
