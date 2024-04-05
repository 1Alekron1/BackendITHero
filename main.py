from flask import Flask, Blueprint
from flask_jwt_extended import JWTManager
from config import JWT_SECRET_KEY

from config import (
    HOST,
    PORT,
    DEBUG,
)
from boss import boss

app: Flask = Flask(__name__)
app.config["JWT_SECRET_KEY"] = JWT_SECRET_KEY
jwt = JWTManager(app)


BLUEPRINTS: list[Blueprint] = [
    boss,
]
for blueprint in BLUEPRINTS:
    app.register_blueprint(blueprint)


if __name__ == "__main__":
    app.run(
        host=HOST,
        port=PORT,
        debug=DEBUG,
    )
