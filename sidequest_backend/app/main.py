from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

import logging
import logging.config
from app.db.session import engine
from app.models import plan as models
from app.api.api_v1.api import api_router
from app.middlewares.middleware import register_middlewares

def create_app() -> FastAPI:
    app = FastAPI(title="SideQuest616", 
                  version="0.1.0", 
                  swagger_ui_parameters={"persistAuthorization": True})
    app.include_router(api_router, prefix="/api/v1")
    return app

app = create_app()

models.Base.metadata.create_all(bind=engine)

logging.config.fileConfig("./app/core/logging.conf")
Instrumentator().instrument(app).expose(app, endpoint="/metrics", include_in_schema=False)
register_middlewares(app)

if __name__ == "__main__":
    import uvicorn
    logging.info("Arrancando SideQuest Backend")
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
