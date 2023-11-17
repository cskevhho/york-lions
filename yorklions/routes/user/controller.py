from flask import Blueprint, render_template, request, redirect, url_for
from .services import create_user, read_user, update_user, delete_all, save_picture
from ...models.user import User

user_ctrl = Blueprint("user", __name__)


@user_ctrl.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        return create_user(username, email, password)

    return render_template("user/create.html")


@user_ctrl.route("/read", methods=["GET", "POST"])
def read():
    if request.method == "POST":
        return read_user(request)

    return render_template("user/read.html")


@user_ctrl.route("/update", methods=["GET", "POST"])
def update():
    if request.method == "POST":
        user_id = request.form.get("id")
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        # Do not pass in objects to the route, pass the parameters in, ORM formalities stuff
        return update_user(
            user_id, {"username": username, "email": email, "password": password}
        )

    return render_template("user/update.html")


@user_ctrl.route("/delete", methods=["GET", "POST"])
def delete():
    if request.method == "POST":
        return delete_all()

    return render_template("user/delete.html")
