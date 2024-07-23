from sqlalchemy import (Column, String, Integer,
                        Float, Boolean, DateTime, ForeignKey)
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    # называем таблицу
    __tablename__ = "users"
    # создаем колонки
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String, unique=True)
    phone_number = Column(String, unique=True)
    reg_date = Column(DateTime)
class Questions(Base):
    __tablename__ = "questions"
    id = Column(Integer, autoincrement=True, primary_key=True)
    q_text = Column(String)
    answer = Column(Integer, nullable=False)
    level = Column(String, default="easy")
    v1 = Column(String, nullable=False)
    v2 = Column(String, nullable=False)
    v3 = Column(String, nullable=True)
    v4 = Column(String, nullable=True)
    reg_date = Column(DateTime)
class Answer(Base):
    __tablename__ = "answer"
    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    question_id = Column(Integer, ForeignKey("questions.id"))
    user_answer = Column(Integer)
    # создаем связи с таблицами
    user_fk = relationship(User)
    question_fk = relationship(Questions)
class Rating(Base):
    __tablename__ = "rating"
    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    user_score = Column(Integer, default=0)
    user_fk = relationship(User)






