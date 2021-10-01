from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.utils import get_db
from user.models import User
from . import service
from typing import List
from .model_pyndantic import TaskCreate, TitleList

router = APIRouter()


@router.get("/", response_model=List[TitleList])
async def tasks_list():
    return await service.get_tasks_list()


@router.post("/")
async def tasks_create(item: TaskCreate):
    return await service.create_task(item)
