from flask import Flask, Blueprint
from flask_jwt_extended import JWTManager
from config import JWT_SECRET_KEY

from config import (
    HOST,
    PORT,
    DEBUG,
)
from endpoints.boss import boss
from endpoints.hr import hr
from endpoints.common import common

app: Flask = Flask(__name__)
app.config["JWT_SECRET_KEY"] = JWT_SECRET_KEY
jwt = JWTManager(app)


BLUEPRINTS: list[Blueprint] = [
    boss,
    hr,
    common,
]
for blueprint in BLUEPRINTS:
    app.register_blueprint(blueprint)


if __name__ == "__main__":
    app.run(
        host=HOST,
        port=PORT,
        debug=DEBUG,
    )
