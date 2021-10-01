from user.model_pyndantic import User, UserCreate, UserUpdate, UserDB
from fastapi_users import FastAPIUsers
from user.logic import jwt_authentication, get_user_manager

fastapi_users = FastAPIUsers(
    get_user_manager,
    [jwt_authentication],
    User,
    UserCreate,
    UserUpdate,
    UserDB,
)
current_active_user = fastapi_users.current_user()

