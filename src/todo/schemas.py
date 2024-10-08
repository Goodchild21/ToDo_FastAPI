from pydantic import BaseModel


class ToDoBase(BaseModel):
    title: str


class ToDo(ToDoBase):
    id: int

    class Config:
        orm_mode = True