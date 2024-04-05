from flask import Flask, Blueprint

from config import (
    HOST,
    PORT,
    DEBUG,
)
from boss import boss

app: Flask = Flask(__name__)

BLUEPRINTS: list[Blueprint] = [
    boss,
]
for blueprint in BLUEPRINTS:
    app.register_blueprint(blueprint)


if __name__ == '__main__':
    app.run(
        host=HOST,
        port=PORT,
        debug=DEBUG,
    )
