import random
from flask import Blueprint, render_template, flash, request
from flask_login import current_user
from .po.read import get_po
from .user.read import get_user
from .address.read import get_address
from .vehicle.update import mark_vehicle_sold

confirmed_order = Blueprint("confirmedorder", __name__)

@confirmed_order.route("/order/<po_id>", methods=["GET", "POST"])
def confirmed(po_id):
    po = get_po(po_id)
    if po == None:
        return render_template("error/404.html"), 404
    
    if current_user != po.user:
        return render_template("error/403.html"), 403

    address = get_address(po.address_id)
    for vehicle in po.vehicles:
        mark_vehicle_sold(vehicle=vehicle)
    
    if request.method == "POST":
        flash("Order confirmed! Bookmark this page to watch its status.", "success")

    return render_template("confirmed-order.html", po=po, address=address)
