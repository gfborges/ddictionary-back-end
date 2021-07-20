from flask import Flask
from flask import jsonify
from werkzeug.exceptions import Forbidden, NotFound


def register_error_handlers(app: Flask):
    app.register_error_handler(NotFound, handle_error)
    app.register_error_handler(Forbidden, handle_error)


def handle_error(e):
    error = dict(message=str(e))
    return jsonify(error), e.code
