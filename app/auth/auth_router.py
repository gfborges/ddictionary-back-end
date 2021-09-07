from flask.json import jsonify
from flask_jwt_extended.utils import create_access_token, get_current_user
from flask_jwt_extended.view_decorators import jwt_required
from app.errors import register_error_handlers
from app.auth.service import AuthService
from werkzeug.exceptions import Forbidden
from app.auth.models import LoginInfo
from flask.blueprints import Blueprint
from flask_pydantic.core import validate


bp = Blueprint("auth", __name__, url_prefix="/auth")
register_error_handlers(bp)


@bp.post("")
@validate()
def auth(body: LoginInfo):
    password = body.password
    username = body.username
    if domain := AuthService.authenticate(
        domain_slug=username, password=password
    ):
        token = create_access_token(
            identity=username,
            additional_claims={"_id": str(domain._id)},
        )
        return {"access_token": token}, 200
    raise Forbidden("Wrong username or password")


@bp.get("/me")
@jwt_required()
def me():
    return jsonify(get_current_user().to_json()), 200
