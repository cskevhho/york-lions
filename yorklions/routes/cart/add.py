from flask import request, session
from ...models.vehicle import Vehicle
from ...extensions import db


def add_vehicle(vehicle_id, quantity):

    vehicle = Vehicle.query.get(vehicle_id)

    if vehicle:
        price = vehicle.price
        total_price = quantity * price

        item_data = {
            'id': vehicle.id,
            'name': vehicle.make,  
            'quantity': quantity,
            'price': price,
            'total_price': total_price
        }

        if 'cart' not in session:
            session['cart'] = []

        session['cart'].append(item_data)
        return item_data, 200 ## trying to return a json object just to see what im getting back
    else:
        return {"message": "No vehicle to add"}, 400
