from fastapi import APIRouter
from app.api.api_v1.endpoints import plans
from app.api.api_v1.endpoints import auth
from app.api.api_v1.endpoints import tags
from app.api.api_v1.endpoints import health
from app.api.api_v1.endpoints import participants
from app.api.api_v1.endpoints import file_manager
api_router = APIRouter()

api_router.include_router(plans.router, prefix="/plans", tags=["plans"])
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(tags.router, prefix="/tags", tags=["tags"])
api_router.include_router(participants.router, prefix="/participants", tags=["participants"])
api_router.include_router(health.router, prefix="/health", tags=["health"])
api_router.include_router(file_manager.router, prefix="/file_manager", tags=["file_manager"])