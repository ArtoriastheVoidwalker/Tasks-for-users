from base.db import database
from model.task_model import tasks
from schema.task_schema import TaskCreate
from model.user_model import User, users
from sqlalchemy import select


async def get_tasks_list():
    return await database.fetch_all(query=tasks.select())


async def get_task(pk: int):
    u = users.alias('user')
    t = tasks.alias('task')
    q = select([u.c.id.label("userId"), u.c.name.label("userName"), t]) \
        .select_from(t.join(u)) \
        .where((t.c.id == pk) & (u.c.id == t.c.user))
    task = await database.fetch_one(q)
    if task is not None:
        task = dict(task)
        return {**task, "user": {"id": task.pop("userId"), "name": task.pop("userName")}}.first()
    return None


async def get_task_list_user(user: User):
    task_list = await database.fetch_all(query=tasks.select().where(tasks.c.user == user.id))
    return [dict(result) for result in task_list]


async def create_task(item: TaskCreate, user: User):
    task = tasks.insert().values(**item.dict(), user=user.id)
    pk = await database.execute(task)
    return {**item.dict(), "id": pk, "user": {"id": user.id}}


async def update_task(pk: int, item: TaskCreate, user: User):
    task = tasks.update().where((tasks.c.id == pk) & (tasks.c.user == user.id)).values(**item.dict())
    return await database.execute(task)


async def delete_task(pk: int, user: User):
    task = tasks.delete().where((tasks.c.id == pk) & (tasks.c.user == user.id))
    return await database.execute(task)
