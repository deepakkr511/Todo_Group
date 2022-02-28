from pydantic import BaseModel
from datetime import date
from typing import List, Optional

from sqlalchemy import false


class UserBase(BaseModel):
  username: str
  email: str
  password: str

class UserDisplay(BaseModel):
  username: str
  email: str
  class Config():
    orm_mode = True

class TodoBase(BaseModel):
  task: str
  assigned_to: str
  due_date: str
  is_completed: str
  group_id:int

# for todo display
class TodoDisplay(BaseModel):
  id: int
  task: str
  assigned_to: str
  due_date: str
  is_completed: str
  group_id: int
  class Config():
    orm_mode = True

class UserAuth(BaseModel):
  id: int
  username: str
  email: str


class GroupBase(BaseModel):
    group_text :str

class GroupDisplay(BaseModel):
    id:int
    group_text: str
    class Config():
        orm_mode = True

