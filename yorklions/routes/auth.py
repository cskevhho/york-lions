from flask import Blueprint, render_template, flash, redirect, url_for
from ..forms import RegistrationForm, LoginForm

auth = Blueprint("auth", __name__)


@auth.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("main.main_index"))
    return render_template("register.html", title="Register", form=form)


@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@ylions.tech" and form.password.data == "password":
            flash("You have been logged in!")
            return redirect(url_for("main.main_index"))
        else:
            flash("Login Unsuccessful. Please check username and password")
    return render_template("login.html", title="Login", form=form)
