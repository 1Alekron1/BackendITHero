from flask import Flask, Blueprint

from config import (
    HOST,
    PORT,
    DEBUG,
)

app: Flask = Flask(__name__)

BLUEPRINTS: list[Blueprint] = [

]
for blueprint in BLUEPRINTS:
    app.register_blueprint(blueprint)


if __name__ == '__main__':
    app.run(
        host=HOST,
        port=PORT,
        debug=DEBUG,
    )
