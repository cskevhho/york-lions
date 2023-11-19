from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from .services import (
    add_vehicle,
    remove_vehicle,
    view_cart,
    checkout_cart,
    submit_order,
)
from ...models.vehicle import Vehicle

cart_ctrl = Blueprint("cart", __name__)


@cart_ctrl.route("/add/", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        vehicle_id = request.args.get("vehicle_id")
        result = add_vehicle(vehicle_id)
        if result[1] != 200:
            flash(result[0]["message"], "danger")
            return redirect(request.referrer)

    return view_cart()


@cart_ctrl.route("/remove", methods=["POST"])
def remove():
    item_id = request.form.get("item_id")
    if remove_vehicle(item_id):
        flash("Item removed successfully", "success")
    else:
        flash("Item not found in cart", "danger")
    return redirect(url_for("cart.view"))


@cart_ctrl.route("/cart", methods=["GET", "POST"])
def view():
    return view_cart()


@cart_ctrl.route("/checkout", methods=["GET", "POST"])
def checkout():
    return checkout_cart()


@cart_ctrl.route("/complete_order", methods=["GET", "POST"])
def complete_order():
    return submit_order()


@cart_ctrl.route("/clear_cart", methods=["POST"])
def clear_cart():
    session["cart"] = []
    return view_cart()
