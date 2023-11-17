from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_user, current_user, logout_user, login_required
from ..forms import RegistrationForm, LoginForm
from ..routes.catalogue import recent, hot_deals as deals

main = Blueprint("main", __name__)

@main.route("/home/")
@main.route("/")
def main_index():
    response = recent.get_recent_vehicles(limit=5)
    if response[1] == 200:
        recent_vehicles = response[0]
    else:
        recent_vehicles = None

    response = deals.get_hot_deals(limit=5)
    if response[1] == 200:
        hot_deals_vehicles = response[0]
    else:
        hot_deals_vehicles = None

    return render_template("index.html", recent_vehicles=recent_vehicles, hot_deals=hot_deals_vehicles)

@main.route("/shop/")
def shop():
    return render_template("index.html")

@main.route("/new-cars/")
def new_cars():
    response = recent.get_recent_vehicles()
    if response[1] == 200:
        recent_vehicles = response[0]
    else:
        recent_vehicles = None

    return render_template("index.html", recent_vehicles=recent_vehicles, show_all=True)

@main.route("/reviews/")
def reviews():
    return render_template("index.html")

@main.route("/trade-in/")
def trade_in():
    return render_template("index.html")

@main.route("/hot-deals/")
def hot_deals():
    response = deals.get_hot_deals()
    if response[1] == 200:
        hot_deals_vehicles = response[0]
    else:
        hot_deals_vehicles = None

    return render_template("index.html", hot_deals=hot_deals_vehicles, show_all=True)

@main.route("/admin/", methods=["GET", "POST"])
def admin_dash():
    if current_user.is_admin == False:              # can comment out, just here for testing purposes
        flash("You are not an admin!", "danger")
        return redirect(url_for("main.main_index"))
    return render_template("admin.html")
