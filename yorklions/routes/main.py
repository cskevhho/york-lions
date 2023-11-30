from flask import Blueprint, render_template, flash, redirect, url_for, request, jsonify
from flask_login import login_user, current_user, logout_user, login_required
from ..forms import RegistrationForm, LoginForm
from ..routes.catalogue import recent, hot_deals as deals, all_vehicles
from .trade_in import create as trade_in_form
from ..routes.vehicle.services import get_vehicle_makes
from ..models.vehicle import Vehicle
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
    sort = request.args.get('sort')
    descending = request.args.get('descending')
    min_price = request.args.get('min_price')
    max_price = request.args.get('max_price')
    condition = request.args.get('condition')
    min_year = request.args.get('min_year')
    max_year = request.args.get('max_year')
    make = request.args.get('make')
    model = request.args.get('model')
    trim = request.args.get('trim')
    colour = request.args.get('colour')

    response = all_vehicles.get_all_vehicles(sort=sort, descending=descending, min_price=min_price, max_price=max_price, condition=condition, min_year=min_year, max_year=max_year, make=make, model=model, trim=trim, colour=colour)
    models_by_make = all_vehicles.get_models_by_make()
    colours = all_vehicles.get_colours()

    if response[1] == 200:
        vehicles = response[0]
    else:
        vehicles = None

    makes = Vehicle.query.distinct(Vehicle.make).all()
    return render_template("listing-view.html", vehicles=vehicles, models_by_make=models_by_make, colours=colours)


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

@main.route("/compare-vehicles" , methods=["GET", "POST"])
def compare_vehicles():
    makes = get_vehicle_makes()
    return render_template("compare-vehicles.html", makes=makes)

@main.route('/get-models')
def get_models():
    selected_make = request.args.get('make')
    models_query = Vehicle.query.with_entities(Vehicle.model).filter_by(make=selected_make).distinct()
    model_names = [model[0] for model in models_query]  # Extracting model names from query results
    return jsonify(model_names)

@main.route("/admin", methods=["GET", "POST"])
def admin_dash():
    if current_user.is_admin == False:              # can comment out, just here for testing purposes
        flash("You are not an admin!", "danger")
        return redirect(url_for("main.main_index"))
    return render_template("admin.html")
