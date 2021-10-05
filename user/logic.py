from core.security import SECRET
from model.user_model import User
from base.db import database
from fastapi_users import BaseUserManager
from typing import Optional
from fastapi_users.db import SQLAlchemyUserDatabase
from fastapi import (
    Depends, Request
)
from schema.user_schema import (
    UserDB, UserCreate
)


users = User.__table__


def get_user_db():
    yield SQLAlchemyUserDatabase(UserDB, database, users)


def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)


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
