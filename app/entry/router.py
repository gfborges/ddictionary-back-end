from flask import Blueprint, jsonify
from flask_pydantic import validate
from werkzeug.exceptions import NotFound
from app.entry.errors import register_error_handlers
from app.entry.models import (
    DomainQuery,
    EntryCreation,
    EntryQuery,
    EntryUpdate,
)
from app.entry.service import EntryService

bp = Blueprint("entry", __name__, url_prefix="/entries")
register_error_handlers(bp)


@bp.get("/all")
@validate()
def list_all(query: DomainQuery):
    entries = EntryService.get_all(query.domain)
    return jsonify([entry.to_simple_json() for entry in entries])


@bp.get("/one")
@validate()
def get_one(query: EntryQuery):
    if entry := EntryService.get_one(**query.dict()):
        return jsonify(entry.to_json())
    raise NotFound("Entry Not Found")


@bp.get("/<string:id>")
def get_entry(id: str):
    if entry := EntryService.get(id):
        return jsonify(entry.to_json())
    print(entry)
    raise NotFound("Entry Not Found")


@bp.post("")
@validate()
def create_entry(body: EntryCreation):
    _id = EntryService.save(entry=body)
    return jsonify(dict(id=str(_id))), 201


@bp.delete("/<string:id>")
@validate()
def delete_entry(id: str):
    EntryService.delete(id=id)
    return jsonify({}), 202


@bp.put("/<string:id>")
@validate()
def update_entry(id: str, body: EntryUpdate):
    EntryService.update(id, body)
    return jsonify({}), 204
