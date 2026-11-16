import os

from flask import Flask

from . import db, routes


def create_app(config=None):
    app = Flask(__name__)
    app.config["DATABASE"] = os.environ.get("DATABASE", "tugas.db")
    if config:
        app.config.update(config)  # dipakai tes untuk DB sementara

    app.teardown_appcontext(db.close_db)
    with app.app_context():
        db.init_db()

    app.register_blueprint(routes.bp)
    return app