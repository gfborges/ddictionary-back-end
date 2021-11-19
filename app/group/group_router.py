from flask_jwt_extended.utils import get_current_user, get_jwt_identity
from flask_jwt_extended.view_decorators import jwt_required
from flask_pydantic.core import validate
from app import group
import app.group.service as group_service
from werkzeug.exceptions import NotFound
from flask import Blueprint
from flask.json import jsonify
from app.group.models import GroupCreation, GroupUpdate

bp = Blueprint(
    "groups",
    __name__,
    url_prefix="/domains/<string:domain_slug>/groups",
)


@bp.get("/<string:group_slug>")
def find_one(domain_slug: str, group_slug: str):
    group = group_service.find_one(
        domain_slug=domain_slug, group_slug=group_slug
    )
    if group:
        return jsonify(group.to_json()), 200
    raise NotFound("Group not found")


@bp.get("")
def find(domain_slug: str):
    groups = group_service.find(domain_slug=domain_slug)
    return jsonify([g.to_json() for g in groups]), 200


@bp.post("")
@jwt_required()
@validate()
def create_group(domain_slug: str, body: GroupCreation):
    domain = get_current_user()
    _id = group_service.save(domain=domain, group_dto=body)
    return jsonify({"_id": str(_id)}), 201


@bp.put("")
@jwt_required()
@validate()
def update_group(domain_slug: str, body: GroupUpdate):
    domain = get_current_user()
    if group_service.update(domain=domain, group_dto=body):
        return jsonify({}), 201
    raise NotFound("Domain not found")
