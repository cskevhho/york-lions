from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from flask_login import current_user
from ...models.trade_in import TradeIn
from ..vehicle.services import create_vehicle
from ...extensions import db
from datetime import datetime
from .utils import trade_in_json

def create_trade_in():
    if request.method == "POST":
        year = request.form["year"]
        make = request.form["make"]
        model = request.form["model"]
        trim = request.form["trim"]
        colour = request.form["colour"]
        type = request.form["type"]
        kilometres = request.form["kilometres"]
        max_range = request.form["max_range"]
        accidents = request.form["accidents"]
        details = request.form["details"]
        
        vehicle_id = int(create_vehicle(
            price=0,
            discount=0,
            year=year,
            make=make,
            model=model,
            trim=trim,
            colour=colour,
            type=type,
            kilometres=kilometres,
            max_range=max_range,
            description="Trade-In",
            is_for_sale=False
        )[0]["message"].split('\'')[1])

        try:
            user_id = request.form["user_id"]
        except:
            user_id=current_user.id

        new_trade_in = TradeIn(
            user_id=user_id,
            vehicle_id=vehicle_id,
            quote=0,
            accidents=accidents,
            details=details,
            date_updated=datetime.now().strftime("%F-%R")
        )

        db.session.add(new_trade_in)
        db.session.commit()

        return trade_in_json([new_trade_in]), 200
    return {"message": ""}, 200