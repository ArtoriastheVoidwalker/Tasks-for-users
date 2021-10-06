from fastapi import APIRouter, Depends
from . import service
from typing import List
from schema.task_schema import TaskCreate, TitleList, TaskSingle
from model.user_model import User
from core.static import current_active_user

router = APIRouter()


@router.get("/", response_model=List[TitleList])
async def tasks_list():
    return await service.get_tasks_list()


@router.post("/", status_code=201, response_model=TaskSingle)
async def post_create(item: TaskCreate, user: User = Depends(current_active_user)):
    return await service.create_task(item, user)


@router.get("/my-tasks", response_model=List[TitleList])
async def posts_user(user: User = Depends(current_active_user)):
    return await service.get_task_list_user(user)


@router.put("/{pk}", status_code=201, response_model=TaskSingle)
async def post_create(
        pk: int, item: TaskCreate, user: User = Depends(current_active_user)
):
    return await service.update_task(pk, item, user)


@router.delete("/{pk}", status_code=204)
async def post_create(pk: int, user: User = Depends(current_active_user)):
    return await service.delete_task(pk, user)
