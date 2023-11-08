from flask import Blueprint
from .extensions import db
from .models import User

main = Blueprint('main', __name__) # this is imported by init.py

@main.route("/user/<name>")
def create_user(name):
    user = User(name=name)
    db.session.add(user)
    db.session.commit()
    
    return "User created."