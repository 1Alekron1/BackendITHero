from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(100))
    is_recruiter = db.Column(db.Boolean)


class Task(db.Model):
    __tablename__ = "tasks"
    id = db.Column(db.Integer, primary_key=True)
    recruiter_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    description = db.Column(db.Text)


class Vacancy(db.Model):
    __tablename__ = "vacancies"
    id = db.Column(db.Integer, primary_key=True)
    theme = db.Column(db.String(100))
    job_title = db.Column(db.String(100))
    location = db.Column(db.String(100))
    salary_range = db.Column(db.String(50))
    privileges = db.Column(db.Text)
    responsibilities = db.Column(db.Text)
    requirements = db.Column(db.Text)


class Recruit(db.Model):
    __tablename__ = "recruits"
    id = db.Column(db.Integer, primary_key=True)
    file_path = db.Column(db.String(255))
    vacancy_id = db.Column(db.Integer, db.ForeignKey("vacancies"))


class Offer(db.Model):
    __tablename__ = "offers"
    id = db.Column(db.Integer, primary_key=True)
    vacancy_id = db.Column(db.Integer, db.ForeignKey("vacancies.id"))
    recruit_id = db.Column(db.Integer, db.ForeignKey("recruits.id"))


class Comment(db.Model):
    __tablename__ = "comments"
    text = db.Column(db.Text)
    recruit_id = db.Column(db.Integer, db.ForeignKey("recruits.id"))
