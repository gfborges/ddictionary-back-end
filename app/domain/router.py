from app.domain.domain import domain_to_json
from app.domain.models import DomainCreation
from flask_pydantic.core import validate
import app.domain.service as DomainService
from werkzeug.exceptions import NotFound
from flask import Blueprint
from flask.json import jsonify

bp = Blueprint("domains", __name__, url_prefix="/domains")


@bp.get("/<string:domain_slug>")
def find_one(domain_slug: str):
    if domain := DomainService.find_one(domain_slug=domain_slug):
        return jsonify(domain_to_json(domain)), 200
    raise NotFound("Domain not found")


@bp.post("")
@validate()
def create_domain(body: DomainCreation):
    _id = DomainService.save(domain=body)
    return jsonify({"_id": str(_id)}), 201
