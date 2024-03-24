from flask import Flask
import hashlib

def configure_app(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
    h = hashlib.new('sha256')
    h.update(b"1234")
    app.config["SECRET_KEY"] = h.digest()
    return app