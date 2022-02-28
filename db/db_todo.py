from fastapi import HTTPException, status
from routers.schemas import TodoBase
from sqlalchemy.orm.session import Session
from db.models import DbTodo
from db.models import DbGroup,DbUser



def create(db: Session, request: TodoBase):#creating todo
  new_todo = DbTodo(
    task = request.task,
    assigned_to = request.assigned_to,
    due_date = request.due_date,
    is_completed=request.is_completed,
    group_id=request.group_id
  )
  db.add(new_todo)
  db.commit()
  db.refresh(new_todo)
  return new_todo

def get_all_todos(db: Session):#to fetch all the groups made
  return db.query(DbTodo).all()

#to delete all todos of particular group id
def delete_grp(db: Session, group_id: int):
  g_todo=[]
  g_todo = db.query(DbTodo).filter(DbTodo.group_id == group_id).all()   #to fetch all the task which having same grp_id
  if not g_todo:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
          detail=f'ToDo with group id {group_id} not found')
  while(g_todo):
    db.delete(g_todo[0])
    g_todo.pop(0)
    db.commit()
  return 'Group is deleted'

#mark all group task as completed or not
def markall(db:Session , group_id:int):
  g_todo=[]
  g_todo = db.query(DbTodo).filter(DbTodo.group_id == group_id).all()   #to fetch all the task which having same grp_id
  if not g_todo:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
          detail=f'ToDo with group id {group_id} not found')
  while(g_todo):
    g_todo[0].is_completed='yes'
    g_todo.pop(0)
    db.commit()
  return 'Marked all as completed'
