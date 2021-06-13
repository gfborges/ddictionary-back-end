from flask import Blueprint, jsonify
from bson import json_util
import app.dictionary.service as dictionary_service

bp = Blueprint(
    "dictionary", __name__, url_prefix="/dictionary/<string:domain>"
)


@bp.get("/")
def list_all(domain: str):
    entries = dictionary_service.get_all(domain)
    return jsonify(entries)


@bp.get("/<string:group>/<string:title>")
def get_one(domain: str, group: str, title: str):
    entry = dictionary_service.get_one(
        domain=domain,
        group=group,
        title=title,
    )
    return jsonify(entry)
