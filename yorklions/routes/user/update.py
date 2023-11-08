from flask import Blueprint
from ...extensions import db
from ...models.user import User

update = Blueprint("update", __name__)  # this is imported by init.py


@update.route("/update/<name>")
def find_user(name):
    # TODO
    
    return "TODO"
