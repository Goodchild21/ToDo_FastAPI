from fastapi import FastAPI

from src.todo.router import router as todo_router
# from src.auth.router import router as auth_router


app = FastAPI()

app.include_router(todo_router)
# app.include_router(auth_router)