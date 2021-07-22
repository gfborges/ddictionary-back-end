from flask_jwt_extended.utils import create_access_token
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
            additional_claims={"_id": str(domain.get("_id"))},
        )
        return {"access_token": token}, 200
    raise Forbidden("Wrong username or password")
