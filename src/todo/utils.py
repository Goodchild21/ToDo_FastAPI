from sqlalchemy.orm import Session

from src.todo.models import ToDo
from src.auth.utils import get_current_user
from src.todo.schemas import ToDoBase


#NEW
def create_todo(db: Session, todo: ToDoBase, token) -> ToDo:
    user = get_current_user(db, token)
    todo = ToDo(
        title=todo.title,
        user_id=user.id
    )
    db.add(todo)
    db.commit()
    return todo


#UPDATE
def update_todo(db: Session, new_todo: ToDo, todo_id: int) -> ToDo:
    todo = db.query(ToDo).filter(ToDo.id == todo_id).first()
    todo.title = new_todo.title
    db.add(todo)
    db.commit()
    return todo


#SELECT ALL
def get_todos(db: Session) -> list[ToDoBase]:
    return db.query(ToDo).all()


#SELECT ALL MY TODOS
def get_my_todos(db: Session, token) -> ToDo:
    user = get_current_user(db, token)
    return db.query(ToDo).filter(ToDo.user_id == user.id).all()


#DEL
def delete_todo_by_id(db: Session, todo_id: int) -> ToDo:
    todo = db.query(ToDo).filter(ToDo.id == todo_id).first()
    db.delete(todo)
    db.commit()
    return todo