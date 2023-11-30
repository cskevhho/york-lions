from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_user, current_user, logout_user, login_required
from ..forms import RegistrationForm, LoginForm
from ..routes.catalogue import recent, hot_deals as deals, all_vehicles
from .trade_in import create as trade_in_form

main = Blueprint("main", __name__)

@main.route("/home")
@main.route("/")
def main_index():
    response = recent.get_recent_vehicles(limit=10)
    if response[1] == 200:
        recent_vehicles = response[0]
    else:
        recent_vehicles = None

    response = deals.get_hot_deals(limit=10)
    if response[1] == 200:
        hot_deals_vehicles = response[0]
    else:
        hot_deals_vehicles = None

    return render_template("index.html", recent_vehicles=recent_vehicles, hot_deals=hot_deals_vehicles)

@main.route("/shop", methods=["GET", "POST"])
def shop():
    sort = request.form.get('sort')
    descending = request.form.get('descending')
    min_price = request.form.get('min_price')
    max_price = request.form.get('max_price')
    condition = request.form.get('condition')
    min_year = request.form.get('min_year')
    max_year = request.form.get('max_year')
    type = request.form.get('type')
    make = request.form.get('make')
    model = request.form.get('model')
    trim = request.form.get('trim')
    colour = request.form.get('colour')

    result, _ = all_vehicles.get_all_vehicles(sort=sort, descending=descending, min_price=min_price, max_price=max_price, condition=condition, min_year=min_year, max_year=max_year, type=type, make=make, model=model, trim=trim, colour=colour)

    return render_template("listing-view.html", vehicle_data=result, search_criteria=request.form)


@main.route("/reviews")
def reviews():
    return render_template("index.html")

@main.route("/trade-in", methods=["GET", "POST"])
def trade_in():
    if request.method == "POST":
        trade_in_form.create_trade_in()
        flash("Trade-in request submitted!", "success")
        return redirect(url_for("main.main_index"))

    return render_template("trade-in.html")

@main.route("/admin", methods=["GET", "POST"])
def admin_dash():
    if current_user.is_admin == False:              # can comment out, just here for testing purposes
        flash("You are not an admin!", "danger")
        return redirect(url_for("main.main_index"))
    return render_template("admin.html")
