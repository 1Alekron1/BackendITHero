from flask import Blueprint, request

__all__ = ("login",)

from flask_jwt_extended import create_access_token

from models import User, session

login: Blueprint = Blueprint("login", __name__)


@login.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    user = session.query(User).filter_by(username=username, password=password).first()
    if not user:
        return {"msg": "Incorrect username or password"}, 403

    access_token = create_access_token(identity=username)
    return {"access_token": access_token}
