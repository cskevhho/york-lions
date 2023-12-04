from flask import Blueprint, render_template, flash, redirect, url_for, request, jsonify, session
from flask_login import login_user, current_user, logout_user, login_required
from ..wtform.vehicle_forms import CreateTradeInForm
from ..routes.catalogue import recent, hot_deals as deals, all_vehicles
from .trade_in import create as trade_in_form
from ..routes.vehicle.services import get_average_rating
from ..routes.catalogue.compare import add_vehicle_to_compare
from ..routes.trade_in.read import get_trade_in
from ..routes.vehicle.read import get_vehicle

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
    sort = request.form.get('sort')
    descending = request.form.get('descending')
    min_price = request.form.get('min_price')
    max_price = request.form.get('max_price')
    condition = request.form.get('condition')
    min_year = request.form.get('min_year')
    max_year = request.form.get('max_year')
    min_range = request.form.get('min_range')
    max_range = request.form.get('max_range')
    min_kilometres = request.form.get('min_kilometres')
    max_kilometres = request.form.get('max_kilometres')
    type = request.form.get('type')
    make = request.form.get('make')
    model = request.form.get('model')
    trim = request.form.get('trim')
    colour = request.form.get('colour')

    result, _ = all_vehicles.get_all_vehicles(sort=sort, descending=descending, min_price=min_price, max_price=max_price, condition=condition, min_year=min_year, max_year=max_year, min_range=min_range, max_range=max_range, min_kilometres=min_kilometres, max_kilometres=max_kilometres, type=type, make=make, model=model, trim=trim, colour=colour)

    return render_template("listing-view.html", vehicle_data=result, search_criteria=request.form)


@main.route("/reviews")
def reviews():
    return render_template("index.html")

@main.route("/admin", methods=["GET", "POST"])
@login_required
def admin_dash():
    if not current_user.is_admin:
        return render_template("error/403.html"), 403
    return render_template("admin.html")

# TODO: Move below routes to a separate file, very much low priority for time
@main.route("/trade-in", methods=["GET", "POST"])
def trade_in():
    form = CreateTradeInForm()
    if form.validate_on_submit():
        trade_in_id = trade_in_form.create_trade_in(form)[0][0]["id"]
        flash("Trade-in request submitted! You will recieve an email shortly with details.", "success")
        return redirect(url_for("main.trade_in_status", trade_in_id=trade_in_id))
    return render_template("trade-in.html", form=form)

@main.route("/trade-in/<trade_in_id>", methods=["GET", "POST"])
@login_required
def trade_in_status(trade_in_id):
    trade_in=get_trade_in(trade_in_id)
    if not trade_in:
        return render_template("error/404.html"), 404
    if trade_in.user_id != current_user.id:
        return render_template("error/403.html"), 403
    vehicle=get_vehicle(trade_in.vehicle_id)
    return render_template("vehicle-details.html", vehicle=vehicle, trade_in=trade_in)

@main.route("/compare-vehicles" , methods=["GET", "POST"])
def compare_vehicles():
    if request.method == "POST":
        if request.form.get("clear_compare") == "true":
            session.pop("compare")
        else:
            add_vehicle_to_compare(request.form.get("vehicle_id"))

    return render_template("vehicle-comparison.html", vehicles=session.get('compare'))

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

def handle_error(error):
    return render_template(f'error/{error.code}.html'), error.code
