from base.db import database
from model.task_model import tasks
from schema.task_schema import TaskCreate


async def get_tasks_list():
    return await database.fetch_all(query=tasks.select())


async def create_task(item: TaskCreate):
    task = tasks.insert().values(**item.dict())
    return await database.execute(task)
