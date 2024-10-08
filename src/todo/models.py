from src.database import Base
from sqlalchemy import Column, Integer, String, Boolean


class ToDo(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)