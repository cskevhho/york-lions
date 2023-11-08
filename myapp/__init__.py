from flask import Flask
from .extensions import db
from .routes.create_route import create
from .routes.read_route import read
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    
    db.init_app(app)
    
    app.register_blueprint(create)
    app.register_blueprint(read)
        
    return app 