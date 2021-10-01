from sqlalchemy.orm import Session

from user.models import User
from core.db import database
from .models import Task, tasks
from .model_pyndantic import TaskCreate


async def get_tasks_list():
    return await database.fetch_all(query=tasks.select())


async def create_task(item: TaskCreate):
    task = tasks.insert().values(**item.dict())
    return await database.execute(task)