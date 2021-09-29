from app.database.escfg import config_es
from app.errors import register_error_handlers
from app.auth.config import config_jwt
from app.database.mongo import get_db, config_mongo
from app.database.cloudinarycfg import config_cloudinary
from flask import Flask, jsonify
from flask_cors import CORS


def register_blueprints(app: Flask):
    from app.entry.entry_router import bp as entry_bp
    from app.domain.domain_router import bp as domain_bp
    from app.auth.auth_router import bp as auth_bp

    app.register_blueprint(entry_bp)
    app.register_blueprint(domain_bp)
    app.register_blueprint(auth_bp)


def config_app(app: Flask):
    CORS(app)
    config_mongo(app)
    config_cloudinary(app)
    config_jwt(app)
    config_es(app)


def create_app():
    app = Flask(__name__)
    config_app(app)
    register_blueprints(app)
    register_error_handlers(app)

    @app.route("/health")
    def app_health():
        health = {
            "api": "ok",
            "mongo": get_db().db.command("ping"),
            "cloudinary": "ok",
        }
        return jsonify(health), 200

    return app
