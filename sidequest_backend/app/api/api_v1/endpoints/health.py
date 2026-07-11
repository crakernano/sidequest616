from fastapi import APIRouter

router = APIRouter()


@router.get("/health", tags=["health"])
def health_check():
    return {"status": "ok"}
