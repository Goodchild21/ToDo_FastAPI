from fastapi import APIRouter, Depends

from src.database import SessionLocal

import src.todo.utils as utils
from src.todo.schemas import ToDoBase, ToDo
from src.auth.utils import oauth2_scheme


router = APIRouter(prefix="/todo", tags=["todo"])

@router.get('/', response_model=list[ToDoBase])
async def get_todos():
    with SessionLocal() as session:
        todos = utils.get_all_todos(session)
    return todos


@router.post('/', response_model=ToDo)
async def create_todo(todo: ToDoBase, token = Depends(oauth2_scheme)):
    with SessionLocal() as session:
        session.expire_on_commit = False
        todo = utils.create_todo(session, todo)
    return todo


@router.put("/{todo_id}", response_model=ToDoBase)
async def update_todo(todo_id: int, todo: ToDoBase, token = Depends(oauth2_scheme)):
    with SessionLocal() as session:
        session.expire_on_commit = False
        todo = utils.update_todo(session, todo, todo_id)
    return todo


@router.delete('/{todo_id}', response_model=ToDo)
async def delete_todo(todo_id: int, token = Depends(oauth2_scheme)):
    with SessionLocal() as session:
        session.expire_on_commit = False
        todo = utils.delete_todo_by_id(session, todo_id)
    return todo