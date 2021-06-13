from flask import Blueprint, jsonify
from app.database.mongo import get_db

bp = Blueprint("dictionary", __name__, url_prefix="/dictionary")
