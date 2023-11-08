from flask import Flask
from yorklions.extensions import db, migrate
from yorklions.routes.user.create import create
from yorklions.routes.user.read import read
from yorklions.routes.user.create import create
from yorklions.routes.user.read import read

# TODO: Blueprint import to combine all 4 operations into one register_blueprint()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(create)
    app.register_blueprint(read)

    return app