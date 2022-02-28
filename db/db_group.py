from fastapi import HTTPException, status
from db.models import DbGroup
from routers.schemas import GroupBase
from sqlalchemy.orm.session import Session

#creating group and adding todo in todo table with refrence to group id
#we can acces all todos of particular group id and then we can perform delete and mark all todo as done or not 
def creategroup(db: Session, request: GroupBase):
  new_group = DbGroup(
    group_text=request.group_text
  )
  db.add(new_group)
  db.commit()
  db.refresh(new_group)
  return new_group

def get_all_group(db: Session):
  return db.query(DbGroup).all()