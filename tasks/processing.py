from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.utils import get_db
from . import service
from typing import List
from .model_pyndantic import TaskCreate, TitleList
router = APIRouter()


@router.get("/", response_model=List[TitleList])
def tasks_list(db: Session = Depends(get_db)):
    return service.get_tasks_list(db)


@router.post("/")
def tasks_list(item: TaskCreate, db: Session = Depends(get_db), ):
    return service.create_task(db, item)
