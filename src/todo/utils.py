from sqlalchemy.orm import Session
from fastapi import Depends

from src.todo.models import ToDo
import src.todo.schemas as schemas
from src.auth.utils import oauth2_scheme #, get_current_user
from src.database import SessionLocal



#NEW
def create_todo(db: Session, todo: schemas.ToDoBase) -> ToDo:
    # token = Depends(oauth2_scheme)
    # with SessionLocal() as session:
    #     user = get_current_user(session, token)
    # user: get_current_user()
    todo = ToDo(
        title=todo.title,
        # user_id=user.id
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
def get_all_todo(db: Session) -> list[ToDo]:
    return db.query(ToDo).all()


#SELECT ID
def get_todo_by_id(db: Session, todo_id: int) -> ToDo:
    return db.query(ToDo).filter(ToDo.id == todo_id).first()


#DEL
def delete_todo_by_id(db: Session, todo_id: int) -> ToDo:
    todo = db.query(ToDo).filter(ToDo.id == todo_id).first()
    db.delete(todo)
    db.commit()
    return todo