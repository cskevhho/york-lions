import random
from flask import Blueprint, render_template, request, redirect, url_for, session
from flask_login import current_user
from .services import create_trade_in, read_trade_ins, update_trade_in, delete_all
from ...models.trade_in import TradeIn
from datetime import datetime

trade_in_ctrl = Blueprint("trade_in", __name__)


@trade_in_ctrl.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":      
        return create_trade_in()

    return render_template("trade_in/create.html")


@trade_in_ctrl.route("/read", methods=["GET", "POST"])
def read():
    if request.method == "POST":
        return read_trade_ins(request)

    return render_template("trade_in/read.html")


@trade_in_ctrl.route("/update", methods=["GET", "POST"])
def update():
    if request.method == "POST":
        trade_in_id = request.form["id"]
        user_id = request.form["user_id"]
        vehicle_id = request.form["vehicle_id"]
        status = request.form["status"]
        quote = request.form["quote"]
        accidents = request.form["accidents"]
        details = request.form["details"]

        # Do not pass in objects to the route, pass the parameters in, ORM formalities stuff
        return update_trade_in (trade_in_id, {
            "id": trade_in_id,
            "user_id": user_id,
            "vehicle_id": vehicle_id,
            "status": status,
            "quote": quote,
            "accidents": accidents,
            "details": details,
            "date_updated": datetime.now().strftime("%F-%R"),
        })

    return render_template("trade_in/update.html")


@trade_in_ctrl.route("/delete", methods=["GET", "POST"])
def delete():
    if request.method == "POST":
        return delete_all()

    return render_template("trade_in/delete.html")
