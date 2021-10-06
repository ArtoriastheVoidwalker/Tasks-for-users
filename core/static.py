from fastapi_users import FastAPIUsers
from user.logic import get_user_manager
from core.security import SECRET
from fastapi_users.authentication import JWTAuthentication
from schema.user_schema import (
    User, UserCreate, UserUpdate, UserDB
)


jwt_authentication = JWTAuthentication(secret=SECRET, lifetime_seconds=3600)
fastapi_users = FastAPIUsers(
    get_user_manager,
    [jwt_authentication],
    User,
    UserCreate,
    UserUpdate,
    UserDB,
)

current_active_user = fastapi_users.current_user(active=True)
