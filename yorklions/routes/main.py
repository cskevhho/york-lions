from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_user, current_user, logout_user, login_required
from ..forms import RegistrationForm, LoginForm

main = Blueprint("main", __name__)

@main.route("/home")
@main.route("/")
def main_index():
    return render_template("index.html")

@main.route("/shop/")
def shop():
    return render_template("index.html")

@main.route("/new-cars/")
def new_cars():
    return render_template("index.html")

@main.route("/reviews/")
def reviews():
    return render_template("index.html")

@main.route("/trade-in/")
def trade_in():
    return render_template("index.html")

@main.route("/hot-deals/")
def hot_deals():
    return render_template("index.html")

@main.route("/admin/", methods=["GET", "POST"])
def admin_dash():
    if current_user.is_admin == False:              # can comment out, just here for testing purposes
        flash("You are not an admin!", "danger")
        return redirect(url_for("main.main_index"))
    return render_template("admin.html")
