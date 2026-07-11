from fastapi import APIRouter
from app.api.api_v1.endpoints import plans
from app.api.api_v1.endpoints import auth
from app.api.api_v1.endpoints import tags
from app.api.api_v1.endpoints import health

api_router = APIRouter()

api_router.include_router(plans.router, prefix="/plans", tags=["plans"])
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(tags.router, prefix="/tags", tags=["tags"])
api_router.include_router(health.router, prefix="/health", tags=["health"])