import random
from flask import Blueprint, render_template
from ..vehicle.services import get_vehicle
from ..vehicle.utils import generate_image_url

vehicle_detail_pages = Blueprint("vehicle_details", __name__)

@vehicle_detail_pages.route("/vehicle/<id>", methods=["GET", "POST"])
def show_detail_page(id):
    vehicle = get_vehicle(id)

    vehicle.image_file = generate_image_url(vehicle)
    return render_template("vehicle-details.html", vehicle=vehicle)