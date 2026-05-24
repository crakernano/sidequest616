from fastapi import APIRouter
from app.api.api_v1.endpoints import plans

api_router = APIRouter()

api_router.include_router(plans.router, prefix="/plans", tags=["plans"])
