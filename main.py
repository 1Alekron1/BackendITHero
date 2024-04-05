from flask import Flask, Blueprint
from flask_jwt_extended import JWTManager

from config import (
    HOST,
    PORT,
    DEBUG,
    JWT_SECRET_KEY,
    JWT_ACCESS_TOKEN_EXPIRES,
)
from models import Base, engine
from endpoints.boss import boss
from endpoints.hr import hr
from endpoints.common import common
from endpoints.login import login

app: Flask = Flask(__name__)
app.config["JWT_SECRET_KEY"] = JWT_SECRET_KEY
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = JWT_ACCESS_TOKEN_EXPIRES
jwt = JWTManager(app)


BLUEPRINTS: list[Blueprint] = [
    login,
    boss,
    hr,
    common,
]
for blueprint in BLUEPRINTS:
    app.register_blueprint(blueprint)


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)  # FixMe
    app.run(
        host=HOST,
        port=PORT,
        debug=DEBUG,
    )
