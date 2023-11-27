from fastapi import APIRouter
from fastapi.responses import FileResponse


router = APIRouter(tags=["Home Route"])


@router.get("/")
async def home():
    return FileResponse("README.md")
