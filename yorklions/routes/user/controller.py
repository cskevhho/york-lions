from flask import Blueprint, render_template, request, redirect, url_for
from .services import create_user, read_user, update_user, delete_all

user_ctrl = Blueprint("user", __name__)


@user_ctrl.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        name = request.form["name"]
        return create_user(name)

    return render_template("user/create.html")


@user_ctrl.route("/read", methods=["GET", "POST"])
def read():
    if request.method == "POST":
        return read_user()

    return render_template("user/read.html")


@user_ctrl.route("/update", methods=["GET", "POST"])
def update():
    if request.method == "POST":
        id = request.form["id"]
        name = request.form["name"]
        return update_user(id)

    return render_template("user/update.html")


@user_ctrl.route("/delete", methods=["GET", "POST"])
def delete():
    if request.method == "POST":
        return delete_all()

    return render_template("user/delete.html")
