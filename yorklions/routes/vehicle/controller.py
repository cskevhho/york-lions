from flask import Blueprint, render_template, request, redirect, url_for
from .services import create_vehicle, read_vehicle, update_vehicle, delete_all
from ...models.vehicle import Vehicle

vehicle_ctrl = Blueprint("vehicle", __name__)


@vehicle_ctrl.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        price = request.form["price"]
        year = request.form["year"]
        make = request.form["make"]
        model = request.form["model"]
        trim = request.form["trim"]
        colour = request.form["colour"]
        type = request.form["type"]
        kilometres = request.form["kilometres"]
        max_range = request.form["max_range"]
        description = request.form["description"]
        return create_vehicle(price, year, make, model, trim, colour, type, kilometres, max_range, description)

    return render_template("vehicle/create.html")


@vehicle_ctrl.route("/read", methods=["GET", "POST"])
def read():
    if request.method == "POST":
        return read_vehicle(request)

    return render_template("vehicle/read.html")


@vehicle_ctrl.route("/update", methods=["GET", "POST"])
def update():
    if request.method == "POST":
        vehicle_id = request.form.get("id")
        price = request.form["price"]
        year = request.form["year"]
        make = request.form["make"]
        model = request.form["model"]
        trim = request.form["trim"]
        colour = request.form["colour"]
        type = request.form["type"]
        kilometres = request.form["kilometres"]
        max_range = request.form["max_range"]
        description = request.form["description"]

        # Do not pass in objects to the route, pass the parameters in, ORM formalities stuff
        return update_vehicle (vehicle_id, {
                "price": price,
                "year": year,
                "make": make,
                "model": model,
                "trim": trim,
                "colour": colour,
                "type": type,
                "kilometres": kilometres,
                "max_range": max_range,
                "description": description
        })

    return render_template("vehicle/update.html")


@vehicle_ctrl.route("/delete", methods=["GET", "POST"])
def delete():
    if request.method == "POST":
        return delete_all()

    return render_template("vehicle/delete.html")
