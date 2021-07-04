from flask.json import jsonify
from app.auth.models import LoginInfo
from flask.blueprints import Blueprint
from flask_pydantic.core import validate


bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.post("")
@validate()
def auth(body: LoginInfo):
    return jsonify(True)
