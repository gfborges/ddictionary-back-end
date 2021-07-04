from flask.blueprints import Blueprint
from flask import jsonify
from werkzeug.exceptions import Forbidden, NotFound


def register_error_handlers(bp: Blueprint):
    bp.register_error_handler(NotFound, handle_error)
    bp.register_error_handler(Forbidden, handle_error)


def handle_error(e):
    error = dict(message=str(e))
    return jsonify(error), e.code
