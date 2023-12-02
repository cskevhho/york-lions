import random
from flask import Blueprint, render_template
from ..vehicle.services import get_vehicle, get_average_rating
from ..vehicle.utils import generate_image_url
from ..rating.read import get_ratings

vehicle_detail_pages = Blueprint("vehicle_details", __name__)

@vehicle_detail_pages.route("/vehicle/<id>", methods=["GET", "POST"])
def show_detail_page(id):
    vehicle = get_vehicle(id)
    if vehicle is None:
        return render_template("404.html"), 404

    make = vehicle.make
    model = vehicle.model
    year = vehicle.year

    average_rating = get_average_rating(make, model, year)
    vehicle.image_file = generate_image_url(vehicle)

    reviews = get_ratings(vehicle)

    return render_template("vehicle-details.html", vehicle=vehicle, average_rating=average_rating, reviews=reviews)

