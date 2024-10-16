from sqlalchemy.orm import Session

from src.todo.models import ToDo
import src.todo.schemas as schemas


#NEW
def create_todo(db: Session, todo: schemas.ToDoBase) -> ToDo:
    todo = ToDo(
        title=todo.title,
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
def get_all_todos(db: Session) -> list[ToDo]:
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
