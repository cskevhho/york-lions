from flask import request, session, flash
from ...models.vehicle import Vehicle
from ...extensions import db


def add_vehicle(vehicle_id):

    vehicle = Vehicle.query.get(vehicle_id)

    if vehicle:
        item_data = {
            'id': vehicle.id,
            'name': f'{vehicle.year} {vehicle.make} {vehicle.model} {vehicle.trim}',  
            'price': vehicle.price,
            'discount': vehicle.discount,
            'total_price': vehicle.price - vehicle.discount
        }

        if 'cart' not in session:
            session['cart'] = []

        for item in session['cart']:
            if item["id"] == vehicle.id:
                return {"message": "Item already in cart"}, 400

        session['cart'].append(item_data)
        session.modified = True
        return item_data, 200 ## trying to return a json object just to see what im getting back
    else:
        return {"message": "No vehicle to add"}, 400
