from fastapi import APIRouter
from tasks import processing

routers = APIRouter()

routers.include_router(processing.router, prefix="/processing")
