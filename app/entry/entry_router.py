from flask_jwt_extended.utils import get_current_user
from flask import Blueprint, jsonify
from flask_pydantic import validate
from werkzeug.exceptions import NotFound
from flask_jwt_extended import jwt_required
from app.entry.repositories.entry_repository import update
from app.entry.services import entry_service
from app.entry.models import (
    DomainQuery,
    EntryCreation,
    EntryQuery,
    EntrySearch,
    EntryUpdate,
)

bp = Blueprint("entry", __name__, url_prefix="/entries")


@bp.get("/all")
@validate()
def list_all(query: DomainQuery):
    entries = entry_service.find_many(query.domain)
    return jsonify([entry.to_json(resumed=True) for entry in entries])


@bp.get("/one")
@validate()
def get_one(query: EntryQuery):
    if entry := entry_service.find_one(query):
        return jsonify(entry.to_json())
    raise NotFound("Entry Not Found")


@bp.get("/search")
@validate()
def search(query: EntrySearch):
    entries = entry_service.search(query)
    return jsonify([entry.to_json(resumed=True) for entry in entries])


@bp.get("/<string:id>")
@jwt_required()
def get_entry(id: str):
    domain = get_current_user()
    if entry := entry_service.find_by_id(domain, id):
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
    domain = get_current_user()
    deleted = entry_service.delete(domain=domain, id=id)
    if not deleted:
        raise NotFound("Entry Not Found")
    return "", 204


@bp.patch("/<string:id>")
@jwt_required()
@validate()
def update_entry(id: str, body: EntryUpdate):
    domain = get_current_user()
    updated = entry_service.update(domain=domain, id=id, entry=body)
    if not updated:
        raise NotFound("Entry Not Found")
    return "", 204
