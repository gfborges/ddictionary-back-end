from app.entry.models import EntryCreation
from flask import Blueprint, json, jsonify
import app.entry.service as entry_service
from flask_pydantic import validate

bp = Blueprint("entry", __name__, url_prefix="/entries/<string:domain>")


@bp.get("")
def list_all(domain: str):
    entries = entry_service.get_all(domain)
    return jsonify(entries)


@bp.post("")
@validate()
def create(domain: str, body: EntryCreation):
    entry_service.save(domain, entry=body.dict())
    return jsonify({}), 201


@bp.get("/<string:group>/<string:title>")
def get_one(domain: str, group: str, title: str):
    entry = entry_service.get_one(
        domain=domain,
        group=group,
        title=title,
    )
    return jsonify(entry)


@bp.delete("/<string:group>/<string:title>")
def delete(domain: str, group: str, title: str):
    entry_service.delete(
        domain=domain,
        group=group,
        title=title,
    )
    return jsonify({}), 202
