from flask_jwt_extended.utils import get_jwt_identity
from flask_jwt_extended.view_decorators import jwt_required
from app.domain.domain import domain_to_json
from app.domain.models import DomainCreation, DomainUpdate
from app.domain import service as domain_service
from flask_pydantic.core import validate
from werkzeug.exceptions import NotFound
from flask import Blueprint
from flask.json import jsonify

bp = Blueprint("domains", __name__, url_prefix="/domains")


@bp.get("/<string:domain_slug>")
def find_one(domain_slug: str):
    if domain := domain_service.find_one(domain_slug=domain_slug):
        return jsonify(domain_to_json(domain)), 200
    raise NotFound("Domain not found")


@bp.post("")
@validate()
def create_domain(body: DomainCreation):
    _id = domain_service.save(domain=body)
    return jsonify({"_id": str(_id)}), 201


@bp.put("")
@validate()
@jwt_required()
def update_domain(body: DomainUpdate):
    domain_slug = get_jwt_identity()
    if domain_service.update(domain_slug, body.group):
        return jsonify({}), 201
    raise NotFound("Domain not found")
