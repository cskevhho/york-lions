import random
from flask import Blueprint, render_template, flash
from .po.read import get_po
from .address.read import get_address
from .vehicle.update import mark_vehicle_sold

confirmed_order = Blueprint("confirmedorder", __name__)

@confirmed_order.route("/order/<po_id>", methods=["GET", "POST"])
def confirmed(po_id):
    po = get_po(po_id)
    if po == None:
        return render_template("404.html")
    address = get_address(po.address_id)
    for vehicle in po.vehicles:
        mark_vehicle_sold(vehicle=vehicle)
    
    flash("Order confirmed! Bookmark this page to watch its status.", "success")
    return render_template("confirmedorder.html", po=po, address=address)
