from fastapi import APIRouter, Request

router = APIRouter()


@router.get("/health", tags=["health"])
def health_check(request: Request):
    return {"status": "ok"}
