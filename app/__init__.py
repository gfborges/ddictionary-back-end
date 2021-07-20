from app.errors import register_error_handlers
from app.auth import config_jwt
from flask import Flask, jsonify
from app.database.mongo import get_db, config_mongo
from app.database.cloudinarycfg import config_cloudinary
from flask_cors import CORS


def register_blueprints(app: Flask):
    from app.entry.router import bp as entry_bp
    from app.domain.router import bp as domain_bp
    from app.auth.router import bp as auth_bp

    app.register_blueprint(entry_bp)
    app.register_blueprint(domain_bp)
    app.register_blueprint(auth_bp)


def create_app():
    app = Flask(__name__)
    CORS(app)
    config_mongo(app)
    register_blueprints(app)
    register_error_handlers(app)
    config_cloudinary(app)
    config_jwt(app)

    @app.route("/health")
    def health():
        health = {
            "api": "ok",
            "mongo": get_db().db.command("ping"),
            "cloudinary": "ok",
        }
        return jsonify(health), 200

    return app
