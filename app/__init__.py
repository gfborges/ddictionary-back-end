from flask import Flask, jsonify
from app.database.mongo import get_db, get_mongo_uri


def register_blueprints(app: Flask):
    from app.dictionary.router import bp as dictionary

    app.register_blueprint(dictionary)


def init_db(app: Flask):
    app.config["MONGO_URI"] = get_mongo_uri()
    get_db().init_app(app)


def create_app():
    app = Flask(__name__)
    init_db(app)
    register_blueprints(app)

    @app.route("/health")
    def health():
        health = {"api": "ok"}
        return jsonify(health), 200

    return app
