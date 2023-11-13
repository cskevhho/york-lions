from flask import Blueprint, render_template
from ..forms import RegistrationForm, LoginForm

main = Blueprint("main", __name__)

dummy_data = []


@main.route("/home")
@main.route("/")
def main_index():
    return render_template("index.html", dummy_data=dummy_data)


@main.route("/admin/", methods=["GET", "POST"])
def home():
    return render_template("admin.html")
