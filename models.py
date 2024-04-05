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
    description = Column(Text)


class Vacancy(Base):
    __tablename__ = "vacancies"
    id = Column(Integer, primary_key=True)
    theme = Column(String(100))
    job_title = Column(String(100))
    location = Column(String(100))
    salary_range = Column(String(50))
    privileges = Column(Text)
    responsibilities = Column(Text)
    requirements = Column(Text)


class Recruit(Base):
    __tablename__ = "recruits"
    id = Column(Integer, primary_key=True)
    file_path = Column(String(255))
    vacancy_id = Column(Integer, ForeignKey("vacancies"))


class Offer(Base):
    __tablename__ = "offers"
    id = Column(Integer, primary_key=True)
    vacancy_id = Column(Integer, ForeignKey("vacancies.id"))
    recruit_id = Column(Integer, ForeignKey("recruits.id"))


class Comment(Base):
    __tablename__ = "comments"
    text = Column(Text)
    recruit_id = Column(Integer, ForeignKey("recruits.id"))
