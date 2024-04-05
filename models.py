from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import Integer, Column, create_engine, ForeignKey, String, Boolean, Text

Base = declarative_base()
engine = create_engine(url="sqlite:///db.db")
session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine,
    )
)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    username = Column(String(50), unique=True)
    password = Column(String(100))
    is_hr = Column(Boolean)


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    hr_id = Column(Integer, ForeignKey("users.id"))
    theme = Column(String(100))
    description = Column(Text)
    salary_range = Column(String(50))
    is_completed = Column(Boolean, default=False)


class Recruit(Base):
    __tablename__ = "recruits"

    id = Column(Integer, primary_key=True)
    task_id = Column(Integer, ForeignKey("tasks.id"))
    step_num = Column(Integer)
    file_path = Column(String(255))
    got_offer = Column(Boolean, default=False)


class Offer(Base):
    __tablename__ = "offers"

    id = Column(Integer, primary_key=True)
    recruit_id = Column(Integer, ForeignKey("recruits.id"))


class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True)
    recruit_id = Column(Integer, ForeignKey("recruits.id"))
    text = Column(Text)
    step_num = Column(Integer)
