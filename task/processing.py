from fastapi import APIRouter
from . import service
from typing import List
from schema.task_schema import TaskCreate, TitleList

router = APIRouter()


@router.get("/", response_model=List[TitleList])
async def tasks_list():
    return await service.get_tasks_list()


@router.post("/")
async def tasks_create(item: TaskCreate):
    return await service.create_task(item)
