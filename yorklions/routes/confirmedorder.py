import random
from flask import Blueprint, render_template
from .po.read import get_po
from .povehicle.read import get_povehicle_by_po_id

confirmed_order = Blueprint("confirmedorder", __name__)

@confirmed_order.route("/checkout/success/<po_id>", methods=["GET", "POST"])
def confirmed(po_id):
    po = get_po(po_id)
    return render_template("confirmedorder.html", po=po)
