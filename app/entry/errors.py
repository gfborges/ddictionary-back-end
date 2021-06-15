from flask.blueprints import Blueprint
from flask import jsonify
from werkzeug.exceptions import NotFound


def register_error_handlers(bp: Blueprint):
    bp.register_error_handler(NotFound, handle_not_found)


def handle_not_found(e):
    error = dict(message=str(e))
    return jsonify(error), 404
