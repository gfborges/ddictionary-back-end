from flask.blueprints import Blueprint
from flask import jsonify
from werkzeug.exceptions import BadRequest


def register_error_handlers(bp: Blueprint):
    bp.register_error_handler(BadRequest, handle_bad_request)


def handle_bad_request(e):
    error = dict(message=str(e))
    return jsonify(error), 404
