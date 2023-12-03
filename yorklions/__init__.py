from flask import Flask
from config import configure_app
from .extensions import db, migrate, bcrypt, login_manager
from .routes.user.controller import user_ctrl
from .routes.vehicle.controller import vehicle_ctrl
from .routes.trade_in.controller import trade_in_ctrl
from .routes.catalogue.vehicle_details import vehicle_detail_pages
from .routes.auth import auth
from .routes.main import main
from .routes.loancalc import loancalc
from .routes.cart.controller import cart_ctrl
from .routes.confirmedorder import confirmed_order

app = Flask(__name__)
app = configure_app(app)


db.init_app(app)
migrate.init_app(app, db)
bcrypt.init_app(app)
login_manager.init_app(app)
app.register_blueprint(main)
app.register_blueprint(auth)
app.register_blueprint(loancalc)
app.register_blueprint(cart_ctrl)
app.register_blueprint(vehicle_detail_pages)
app.register_blueprint(confirmed_order)
app.register_blueprint(user_ctrl, url_prefix="/api/user")
app.register_blueprint(vehicle_ctrl, url_prefix="/api/vehicle")
app.register_blueprint(trade_in_ctrl, url_prefix="/api/trade_in")

# This does not overwrite existing tables, just creates new ones if need be.
with app.app_context():
    db.create_all()
