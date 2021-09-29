from flask_jwt_extended.utils import get_current_user
from app import domain
from flask import Blueprint, jsonify
from flask_pydantic import validate
from werkzeug.exceptions import NotFound
from flask_jwt_extended import jwt_required
from app.entry.services import entry_service
from app.entry.models import (
    DomainQuery,
    EntryCreation,
    EntryQuery,
    EntryUpdate,
)

bp = Blueprint("entry", __name__, url_prefix="/entries")


@bp.get("/all")
@validate()
def list_all(query: DomainQuery):
    entries = entry_service.get_all(query.domain)
    return jsonify([entry.to_json(resumed=True) for entry in entries])


@bp.get("/one")
@validate()
def get_one(query: EntryQuery):
    if entry := entry_service.get_one(**query.dict()):
        return jsonify(entry.to_json())
    raise NotFound("Entry Not Found")


@bp.get("/<string:id>")
def get_entry(id: str):
    if entry := entry_service.get(id):
        return jsonify(entry.to_json())
    raise NotFound("Entry Not Found")


@bp.post("")
@jwt_required()
@validate()
def create_entry(body: EntryCreation):
    curr_domain = get_current_user()
    _id = entry_service.save(domain=curr_domain, entry_dto=body)
    return jsonify({"_id": str(_id)}), 201


@bp.delete("/<string:id>")
@jwt_required()
@validate()
def delete_entry(id: str):
    result = entry_service.delete(id=id)
    deleted = result.deleted_count > 0
    if not deleted:
        raise NotFound("Entry Not Found")
    return jsonify({}), 202


@bp.put("/<string:id>")
@jwt_required()
@validate()
def update_entry(id: str, body: EntryUpdate):
    result = entry_service.update(id=id, entry=body)
    updated = result.modified_count > 0
    if not updated:
        raise NotFound("Entry Not Found")
    return jsonify({}), 201
