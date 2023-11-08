from flask import Blueprint
from ...extensions import db
from ...models.user import User

create = Blueprint('create', __name__) # this is imported by init.py

@create.route("/create/<name>")
def create_user(name):
    user = User(name=name)
    db.session.add(user)
    db.session.commit()
    
    return "User created."