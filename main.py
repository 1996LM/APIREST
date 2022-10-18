#primero van las importaciones del framework
from fastapi import FastAPI

#despues las importaciones del proyecto
from app.v1.router.user_router import router as user_router
from app.v1.router.todo_router import router as todo_router


#y despues las importaciones de python

app = FastAPI()

app.include_router(user_router)
app.include_router(todo_router)