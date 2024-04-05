from flask import Flask, Blueprint
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flasgger import Swagger

from config import (
    HOST,
    PORT,
    DEBUG,
    JWT_SECRET_KEY,
    JWT_ACCESS_TOKEN_EXPIRES,
)
from models import session, Base, engine, User
from endpoints.boss import boss
from endpoints.hr import hr
from endpoints.common import common
from endpoints.login import login

app: Flask = Flask(__name__)
app.config["JWT_SECRET_KEY"] = JWT_SECRET_KEY
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = JWT_ACCESS_TOKEN_EXPIRES
jwt = JWTManager(app)
swagger = Swagger(app)

CORS(app)

BLUEPRINTS: list[Blueprint] = [
    login,
    boss,
    hr,
    common,
]
for blueprint in BLUEPRINTS:
    app.register_blueprint(blueprint)


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data) -> User | None:
    identity: str = jwt_data["sub"]
    try:
        user = session.query(User).filter_by(username=identity).first()
        return user
    except ValueError:
        return None


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)  # FixMe
    app.run(
        host=HOST,
        port=PORT,
        debug=DEBUG,
    )
