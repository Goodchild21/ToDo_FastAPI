from fastapi.params import Depends
from pydantic import BaseModel


class ToDoBase(BaseModel):
    title: str


class ToDo(ToDoBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True