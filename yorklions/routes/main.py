from flask import Blueprint, render_template
from ..forms import RegistrationForm, LoginForm

main = Blueprint("main", __name__)

dummy_data = []


@main.route("/home")
@main.route("/")
def main_index():
    return render_template("index.html", dummy_data=dummy_data)

@main.route("/shop/")
def shop():
    return render_template("index.html", dummy_data=dummy_data)

@main.route("/new-cars/")
def new_cars():
    return render_template("index.html", dummy_data=dummy_data)

@main.route("/reviews/")
def reviews():
    return render_template("index.html", dummy_data=dummy_data)

@main.route("/tradein/")
def trade_in():
    return render_template("index.html", dummy_data=dummy_data)

@main.route("/hot-deals/")
def hot_deals():
    return render_template("index.html", dummy_data=dummy_data)

@main.route("/admin/", methods=["GET", "POST"])
def admin_dash():
    return render_template("admin.html")
