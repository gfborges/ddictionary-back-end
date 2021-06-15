from flask import Blueprint, jsonify
from flask_pydantic import validate
from werkzeug.exceptions import NotFound
from app.entry.errors import register_error_handlers
from app.entry.models import DomainQuery, EntryCreation, EntryQuery
import app.entry.service as entry_service

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
        print(entry.json())
        return jsonify(entry.json())
    raise NotFound("Entry Not Found")


@bp.delete("")
@validate()
def delete(query: EntryQuery):
    entry_service.delete(**query.dict())
    return jsonify({}), 202
