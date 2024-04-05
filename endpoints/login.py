from flask import Blueprint, request
from flasgger import swag_from

__all__ = ("login",)

from flask_jwt_extended import create_access_token

from models import User, session

login: Blueprint = Blueprint("login", __name__)


@login.route("/login", methods=["POST"])
@swag_from({
    'tags': ['Login'],
    'summary': 'User Login',
    'description': 'Endpoint for user authentication and login.',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'description': 'User credentials',
            'schema': {
                'type': 'object',
                'properties': {
                    'username': {'type': 'string'},
                    'password': {'type': 'string'}
                }
            }
        }
    ],
    'responses': {
        200: {'description': 'Login successful'},
        403: {'description': 'Incorrect username or password'}
    }
})
def login_():
    username: str = request.json.get("username", None)
    password: str = request.json.get("password", None)
    user: User = session.query(User).filter_by(username=username, password=password).first()
    if not user:
        return {"msg": "Incorrect username or password"}, 403

    access_token = create_access_token(identity=username)
    return {"accessToken": access_token}
