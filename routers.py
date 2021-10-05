from fastapi import APIRouter
from task import processing
from fastapi import FastAPI
from core.static import (
    fastapi_users, jwt_authentication
)


routers = APIRouter()
app = FastAPI()

routers.include_router(processing.router, prefix="/processing")
app.include_router(routers)
app.include_router(
    fastapi_users.get_auth_router(jwt_authentication), prefix="/auth/jwt", tags=["auth"]
)
app.include_router(
    fastapi_users.get_register_router(), prefix="/auth", tags=["auth"]
)
app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_verify_router(),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(fastapi_users.get_users_router(), prefix="/users", tags=["users"])
