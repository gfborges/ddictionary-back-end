from app.entry.errors import register_error_handlers, BadRequest
from app.entry.models import DomainQuery, EntryCreation, EntryQuery
from flask import Blueprint, jsonify
import app.entry.service as entry_service
from flask_pydantic import validate

bp = Blueprint("entry", __name__, url_prefix="/entries")
register_error_handlers(bp)


@bp.get("/all")
@validate()
def list_all(query: DomainQuery):
    entries = entry_service.get_all(query.domain)
    return jsonify(entries)


@bp.post("")
@validate()
def create(body: EntryCreation):
    entry_service.save(entry=body.dict())
    return jsonify({}), 201


@bp.get("")
@validate()
def get_one(query: EntryQuery):
    if entry := entry_service.get_one(**query.dict()):
        return jsonify(entry)
    raise BadRequest("Entry Not Found")


@bp.delete("")
@validate()
def delete(query: EntryQuery):
    entry_service.delete(
        domain=query.domain,
        group=query.group,
        title=query.title,
    )
    return jsonify({}), 202
