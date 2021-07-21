from app.errors import register_error_handlers
from app.domain.models import DomainCreation
from flask_pydantic.core import validate
import app.domain.service as DomainService
from werkzeug.exceptions import NotFound
from flask import Blueprint
from flask.json import jsonify

bp = Blueprint("domains", __name__, url_prefix="/domains")


@bp.get("/<string:domain_name>")
def find_one(domain_name: str):
    if domain := DomainService.find_one(domain_name=domain_name):
        return jsonify(domain.to_json()), 200
    raise NotFound("Domain not found")


@bp.post("")
@validate()
def create_domain(body: DomainCreation):
    _id = DomainService.save(domain=body)
    return jsonify({"id": _id}), 200
