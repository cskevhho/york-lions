from flask import Flask
from .extensions import db, migrate
from .routes.user.controller import user_ctrl
from .routes.index import index

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
    app.config['SECRET_KEY'] = '1234'; # we will hash this once live
    db.init_app(app)
    migrate.init_app(app, db)
    
    app.register_blueprint(index)
    app.register_blueprint(user_ctrl, url_prefix='/user')

    return app
