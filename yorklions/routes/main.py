from flask import Blueprint, render_template, flash, redirect, url_for, request, jsonify
from flask_login import login_user, current_user, logout_user, login_required
from ..forms import RegistrationForm, LoginForm
from ..routes.catalogue import recent, hot_deals as deals, all_vehicles
from .trade_in import create as trade_in_form
from ..routes.vehicle.services import get_vehicle_makes, get_average_rating

from ..models.vehicle import Vehicle
from ..routes.vehicle.utils import generate_image_url


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

@main.route("/admin", methods=["GET", "POST"])
def admin_dash():
    if current_user.is_admin == False:              # can comment out, just here for testing purposes
        flash("You are not an admin!", "danger")
        return redirect(url_for("main.main_index"))
    return render_template("admin.html")

# TODO: Move below routes to a separate file, very much low priority for time
@main.route("/compare-vehicles" , methods=["GET", "POST"])
def compare_vehicles():
    makes = get_vehicle_makes()
    return render_template("compare-vehicles.html", makes=makes)

# AJAX stuff
@main.route('/get-models')
def get_models():
    selected_make = request.args.get('make')
    models_query = Vehicle.query.with_entities(Vehicle.model).filter_by(make=selected_make).distinct()
    model_names = [model[0] for model in models_query]
    return jsonify(model_names)

# AJAX stuff
@main.route('/get-years')
def get_years():
    selected_make = request.args.get('make')
    selected_model = request.args.get('model')
    years_query = Vehicle.query.with_entities(Vehicle.year).filter_by(make=selected_make, model=selected_model).distinct()
    years = [year[0] for year in years_query]
    return jsonify(years)

@main.route('/get-vehicle-id')
def get_vehicle_id():
    make = request.args.get('make')
    model = request.args.get('model')
    year = int(request.args.get('year'))
    vehicle = Vehicle.query.filter_by(make=make, model=model, year=year).first()
    if vehicle:
        return jsonify({'id': vehicle.id})
    return jsonify({'id': None})

@main.route("/vehicle-comparison")
def vehicle_comparison():
    v1_id = request.args.get('vid1')
    v2_id = request.args.get('vid2')

    v1 = Vehicle.query.get(v1_id)
    v2 = Vehicle.query.get(v2_id)
    v1.image_file = generate_image_url(v1)
    v2.image_file = generate_image_url(v2)
    v1rating = get_average_rating(v1.make, v1.model, v1.year)
    v2rating = get_average_rating(v2.make, v2.model, v2.year)
    if not v1 or not v2:
        flash("One or both vehicles not found", "error")
        return redirect(url_for('main.compare_vehicles'))

    return render_template("vehicle-comparison.html", v1=v1, v2=v2, v1rating=v1rating, v2rating=v2rating)








