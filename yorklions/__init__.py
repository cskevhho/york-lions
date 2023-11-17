from flask import Flask
from .extensions import db, migrate, bcrypt, login_manager
from .routes.user.controller import user_ctrl
from .routes.vehicle.controller import vehicle_ctrl
from .routes.auth import auth
from .routes.main import main
from .routes.loancalc import loancalc

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
app.config["SECRET_KEY"] = "1234"


db.init_app(app)
migrate.init_app(app, db)
bcrypt.init_app(app)
login_manager.init_app(app)
app.register_blueprint(main)
app.register_blueprint(auth)
app.register_blueprint(loancalc)
app.register_blueprint(user_ctrl, url_prefix="/api/user")
app.register_blueprint(vehicle_ctrl, url_prefix="/api/vehicle")

with app.app_context():
    db.create_all()