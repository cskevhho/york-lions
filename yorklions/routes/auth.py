from flask import Blueprint, render_template
from ..forms import RegistrationForm, LoginForm

auth = Blueprint("auth", __name__)


@auth.route("/register", methods=["GET","POST"])
def register():
    form = RegistrationForm()
    return render_template("register.html", title="Register", form=form)


@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    return render_template("login.html", title="Login", form=form)