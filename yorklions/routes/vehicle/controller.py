import random
from flask import Blueprint, render_template, request, redirect, url_for, session
from .services import create_vehicle, read_vehicles, update_vehicle, delete_all
from .create import create_vehicle_from_form
from ...wtform.vehicle_forms import CreateVehicleForm


vehicle_ctrl = Blueprint("vehicle", __name__)

@vehicle_ctrl.route("/create", methods=["GET", "POST"])
def create():
    form = CreateVehicleForm()
    if form.validate_on_submit():
        return create_vehicle_from_form(form)
    return render_template("vehicle/create.html", form=form)


@vehicle_ctrl.route("/read", methods=["GET", "POST"])
def read():
    if request.method == "POST":
        return read_vehicles(request)

    return render_template("vehicle/read.html")


@vehicle_ctrl.route("/update", methods=["GET", "POST"])
def update():
    if request.method == "POST":
        vehicle_id = request.form.get("id")
        price = request.form["price"]
        discount = request.form["discount"]
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
                "discount": discount,
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


@vehicle_ctrl.route("/create_dummy_data", methods=["GET", "POST"])
def create_dummy_data():
    add_discount = 0
    for i in range(10):
        price = random.randint(500000, 15000000) / 100.0
        if (add_discount % 3 == 0):
            discount = random.randint(0, int(price-1) * 100) / 200.0
        else:
            discount = 0
        add_discount += 1
        year = random.randint(2012, 2023)
        cars = [
            {"make": "Chevrolet", "model": "Bolt", "trim": "LT", "vehicle_type": "Hatchback"},
            {"make": "Tesla", "model": "Model 3", "trim": "Long Range", "vehicle_type": "Sedan"},
            {"make": "Tesla", "model": "Model X", "trim": "Plaid", "vehicle_type": "SUV"},
            {"make": "Hyundai", "model": "Kona", "trim": "Limited", "vehicle_type": "Crossover"},
            {"make": "Kia", "model": "Soul", "trim": "Luxury", "vehicle_type": "Crossover"},
            {"make": "Nissan", "model": "Leaf", "trim": "SV", "vehicle_type": "Hatchback"},
            {"make": "Rivian", "model": "R1T", "trim": "Adventure", "vehicle_type": "Pickup"},
        ]
        car = cars[random.randrange(len(cars))]
        colours = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Pink", "Black", "White", "Grey"]
        colour = colours[random.randrange(len(colours))]
        kilometres = random.randrange(200000)
        max_range = random.randint(100, 700)
        description = "It's a used " + car["model"]

        date_year = random.randint(2020, 2023)
        date_month = random.randint(1, 12)
        date_day = random.randint(1, 31)
        date_hour = random.randint(0, 23)
        date_minute = random.randint(0, 59)
        date_added = f'{date_year}{("-0" if date_month < 10 else "-")}{date_month}{("-0" if date_day < 10 else "-")}{date_day}{("-0" if date_hour < 10 else "-")}{date_hour}{(":0" if date_minute < 10 else ":")}{date_minute}'
        create_vehicle(price, discount, year, car["make"], car["model"], car["trim"], colour, car["vehicle_type"], kilometres, max_range, description, date_added)

    for i in range(10):
        price = random.randint(3000000, 15000000) / 100.0
        if (add_discount % 3 == 0):
            discount = random.randint(0, int(price-1) * 100) / 200.0
        else:
            discount = 0
        add_discount += 1
        year = 2024
        cars = [
            {"make": "Chevrolet", "model": "Bolt", "trim": "LT", "vehicle_type": "Hatchback"},
            {"make": "Tesla", "model": "Model 3", "trim": "Long Range", "vehicle_type": "Sedan"},
            {"make": "Tesla", "model": "Model X", "trim": "Plaid", "vehicle_type": "SUV"},
            {"make": "Hyundai", "model": "Kona", "trim": "Limited", "vehicle_type": "Crossover"},
            {"make": "Kia", "model": "Soul", "trim": "Luxury", "vehicle_type": "Crossover"},
            {"make": "Nissan", "model": "Leaf", "trim": "SV", "vehicle_type": "Hatchback"},
            {"make": "Rivian", "model": "R1T", "trim": "Adventure", "vehicle_type": "Pickup"},
        ]
        car = cars[random.randrange(len(cars))]
        colours = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Pink", "Black", "White", "Grey"]
        colour = colours[random.randrange(len(colours))]
        kilometres = 0
        max_range = random.randint(300, 700)
        description = "It's a new " + car["model"]

        date_year = random.randint(2020, 2023)
        date_month = random.randint(1, 12)
        date_day = random.randint(1, 31)
        date_hour = random.randint(0, 23)
        date_minute = random.randint(0, 59)
        date_added = f'{date_year}{("-0" if date_month < 10 else "-")}{date_month}{("-0" if date_day < 10 else "-")}{date_day}{("-0" if date_hour < 10 else "-")}{date_hour}{(":0" if date_minute < 10 else ":")}{date_minute}'
        create_vehicle(price, discount, year, car["make"], car["model"], car["trim"], colour, car["vehicle_type"], kilometres, max_range, description, date_added)

    return redirect(url_for('main.admin_dash'))
