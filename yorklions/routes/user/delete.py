from flask import Blueprint
from ...extensions import db
from ...models.user import User

delete = Blueprint("delete", __name__)  # this is imported by init.py


@delete.route("/delete/<name>")
def find_user(name):
    # TODO
    
    return "TODO"
