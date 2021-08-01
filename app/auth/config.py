from app.config import Auth
from app.domain import service as domain_service
from flask_jwt_extended import JWTManager
from flask import Flask

jwt = JWTManager()


def config_jwt(app: Flask):
    jwt.init_app(app)
    app.config["JWT_SECRET_KEY"] = Auth.JWT_SECRET


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return domain_service.find_one(identity)
