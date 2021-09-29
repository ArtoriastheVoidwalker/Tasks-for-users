from fastapi_users.authentication import JWTAuthentication
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from .models import User
from .model_pyndantic import UserDB, UserCreate
from core.db import database
from fastapi_users import BaseUserManager
from typing import Optional
from fastapi import Depends, Request

users = User.__table__


def get_user_db():
    yield SQLAlchemyUserDatabase(UserDB, database, users)


SECRET = "fferbfbt54643d56d4sf6b54nv464d3"

jwt_authentication = JWTAuthentication(secret=SECRET, lifetime_seconds=3600)


class UserManager(BaseUserManager[UserCreate, UserDB]):
    user_db_model = UserDB
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(self, user: UserDB, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")

    async def on_after_forgot_password(
            self, user: UserDB, token: str, request: Optional[Request] = None
    ):
        print(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(
            self, user: UserDB, token: str, request: Optional[Request] = None
    ):
        print(f"Verification requested for user {user.id}. Verification token: {token}")


def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)


# SECRET = "SECRET"
# users = User.__table__
#
# user_db = SQLAlchemyUserDatabase(UserDB, SessionLocal, users)
#
# auth_backends = []
#
# jwt_authentication = JWTAuthentication(secret=SECRET, lifetime_seconds=3600)
#
# auth_backends.append(jwt_authentication)
