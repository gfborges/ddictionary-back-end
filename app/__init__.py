from flask import Flask, jsonify
from app.database.mongo import get_db, get_mongo_uri
from flask_cors import CORS


def register_blueprints(app: Flask):
    from app.entry.router import bp as entry_bp

    app.register_blueprint(entry_bp)


def init_db(app: Flask):
    app.config["MONGO_URI"] = get_mongo_uri()
    get_db().init_app(app)


def create_app():
    app = Flask(__name__)
    CORS(app)
    init_db(app)
    register_blueprints(app)

    @app.route("/health")
    def health():
        health = {
            "api": "ok",
            "mongo": get_db().db.command("ping"),
        }
        return jsonify(health), 200

    return app
