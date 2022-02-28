from routers.schemas import GroupBase,GroupDisplay
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from db.database import get_db
from db import db_group
from typing import List
from fastapi import HTTPException, status
from db.models import DbTodo
router = APIRouter(
    prefix='/group',
    tags=['group']
)

#create group of particular type and add todo in todo table with respective group id
@router.post('',response_model=GroupDisplay)
def create_group(request:GroupBase,db:Session = Depends(get_db)):
    return db_group.creategroup(db,request)

#get all the group name 
@router.get('/all', response_model=List[GroupDisplay])
def Group(db: Session = Depends(get_db)):
  return db_group.get_all_group(db)

