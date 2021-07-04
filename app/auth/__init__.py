from app.config import Auth
from flask_jwt_extended import JWTManager
from flask import Flask

jwt = JWTManager()


def config_jwt(app: Flask):
    jwt.init_app(app)
    app.config["JWT_SECRET_KEY"] = Auth.JWT_SECRET
