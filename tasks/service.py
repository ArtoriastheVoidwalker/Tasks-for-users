from sqlalchemy.orm import Session
from .models import Task
from .model_pyndantic import TaskCreate


def get_tasks_list(db: Session):
    return db.query(Task).all()


def create_task(db: Session, item: TaskCreate):
    task = Task(**item.dict())
    db.add(task)
    db.commit()
    db.refresh(task)
    return task
