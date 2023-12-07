from flask import request
from flask_login import current_user
from ...wtform.vehicle_forms import CreateTradeInForm
from ...models.trade_in import TradeIn
from ..vehicle.services import create_vehicle, get_vehicle
from ...extensions import db
from datetime import datetime
from .utils import trade_in_json
from ...routes.vehicle.utils import generate_image_url
from ..vehicle.create import save_picture


def create_trade_in(form: CreateTradeInForm):
    if request.method == "POST":
        year = form.year.data
        make = form.make.data
        model = form.model.data
        trim = form.trim.data
        colour = form.colour.data
        type = form.type.data
        kilometres = form.kilometres.data
        max_range = form.max_range.data
        accidents = form.accidents.data
        details = form.details.data
        
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
            is_for_sale=False,
        )[0]["new_vehicle_id"])


        pic_file = save_picture(form.picture.data)
        vehicle = get_vehicle(vehicle_id)
        vehicle.image_file = pic_file
        vehicle.image_file = generate_image_url(vehicle)

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
