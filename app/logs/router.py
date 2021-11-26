from werkzeug.exceptions import NotFound
from flask import Blueprint
from flask.json import jsonify
from app import logs
from app.logs import service as logs_service

bp = Blueprint(
    "logs",
    __name__,
    url_prefix="/domains/<string:domain_slug>/logs",
)


@bp.get("/<string:log_cat>")
def find_one(domain_slug: str, log_cat: str):
    logger = logs_service.find_one(domain_slug, log_cat)
    if logger:
        return jsonify(logger.to_json()), 200
    raise NotFound("Logger not found")
