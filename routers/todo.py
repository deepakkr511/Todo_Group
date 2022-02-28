from auth.oauth2 import get_current_user
from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_todo
from typing import List
from routers.schemas import TodoBase, TodoDisplay,UserAuth


router = APIRouter(
  prefix='/post',
  tags=['todo']
)


#create todo having particular group id
@router.post('create_todo', response_model=TodoDisplay)
def create(request: TodoBase, db: Session = Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
  if not request.task:
    raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, 
              detail="Task cannot be Empty")
  return db_todo.create(db, request)

#get all todo irresepective of group id
@router.get('/all', response_model=List[TodoDisplay])
def todos(db: Session = Depends(get_db)):
  return db_todo.get_all_todos(db)

#delete all todos of particular group id
@router.get('/delete_group/{grp_id}')
def delete_todo_grp(grp_id: int, db: Session = Depends(get_db)):#, current_user: UserAuth = Depends(get_current_user)):
  return db_todo.delete_grp(db, grp_id)#,current_user.id)

@router.get('/mark_all/{grp_id}')
def mark_all(grp_id: int, db: Session = Depends(get_db)):#, current_user: UserAuth = Depends(get_current_user)):
  return db_todo.markall(db, grp_id)#,current_user.id)