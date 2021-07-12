from app.entry.entry import entry_to_json, entry_to_simple_json
from flask import Blueprint, jsonify
from flask_pydantic import validate
from werkzeug.exceptions import NotFound
from app.errors import register_error_handlers
from app.entry.models import (
    DomainQuery,
    EntryCreation,
    EntryQuery,
    EntryUpdate,
)
from app.entry.services import entry_service

bp = Blueprint("entry", __name__, url_prefix="/entries")
register_error_handlers(bp)


@bp.get("/all")
@validate()
def list_all(query: DomainQuery):
    entries = entry_service.get_all(query.domain)
    return jsonify([entry_to_simple_json(**entry) for entry in entries])


@bp.get("/one")
@validate()
def get_one(query: EntryQuery):
    if entry := entry_service.get_one(**query.dict()):
        return jsonify(entry_to_json(**entry))
    raise NotFound("Entry Not Found")


@bp.get("/<string:id>")
def get_entry(id: str):
    if entry := entry_service.get(id):
        return jsonify(entry_to_json(**entry))
    raise NotFound("Entry Not Found")


@bp.post("")
@validate()
def create_entry(body: EntryCreation):
    _id = entry_service.save(entry=body)
    return jsonify({"_id": str(_id)}), 201


@bp.delete("/<string:id>")
@validate()
def delete_entry(id: str):
    entry_service.delete(id=id)
    return jsonify({}), 202


@bp.put("/<string:id>")
@validate()
def update_entry(id: str, body: EntryUpdate):
    entry_service.update(id, body)
    return jsonify({}), 204
