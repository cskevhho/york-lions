from flask import Blueprint
from ...extensions import db
from ...models.user import User

read = Blueprint("read", __name__)  # this is imported by init.py


@read.route("/read/<name>")
def find_user(name):
    user = User.query.filter_by(name=name).first()

    if user is None:
        return {"message": "User does not exist."}

    return {"user": user.name}
