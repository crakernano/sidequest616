from fastapi import APIRouter
from app.api.api_v1.endpoints import plans
from app.api.api_v1.endpoints import auth

api_router = APIRouter()

api_router.include_router(plans.router, prefix="/plans", tags=["plans"])
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])