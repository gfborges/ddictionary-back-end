from app.domain.service import DomainService
from flask import Blueprint
from flask.json import jsonify

bp = Blueprint("domains", __name__, url_prefix="/domains")


@bp.get("/<string:domain_name>")
def find_one(domain_name: str):
    domain = DomainService.find_one(domain_name=domain_name)
    return jsonify(domain.to_json()), 200
