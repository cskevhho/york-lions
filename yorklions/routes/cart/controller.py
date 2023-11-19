from flask import Blueprint, render_template, request, redirect, url_for, session
from .services import add_vehicle, remove_vehicle, view_cart
from ...models.vehicle import Vehicle

cart_ctrl = Blueprint("cart", __name__)

@cart_ctrl.route("/add/", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        vehicle_id = request.args.get('vehicle_id')
        quantity = int(request.form.get('quantity'))
        return add_vehicle(vehicle_id, quantity)

    return render_template("cart.html")

@cart_ctrl.route("/remove", methods=["GET", "POST"])
def remove():
    if request.method == "POST":
        return remove_vehicle()

    return render_template("cart.html")

@cart_ctrl.route("/view", methods=["GET", "POST"])
def view():
    return view_cart()