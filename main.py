from fastapi import FastAPI
from db import models
from db.database import engine
from routers import user,todo,group
from auth import authentication
app = FastAPI()


app.include_router(user.router)
app.include_router(todo.router)
app.include_router(group.router)
app.include_router(authentication.router)

models.Base.metadata.create_all(engine)