from ...models.vehicle import Vehicle
from ...routes.vehicle.utils import vehicle_json
from ...routes.vehicle.read import get_vehicle
from flask import session

def add_vehicle_to_compare(vehicle_id):
    vehicle = get_vehicle(vehicle_id)
    if vehicle:
        if 'compare' not in session:
            session['compare'] = []

        for item in session['compare']:
            if item["id"] == vehicle.id:
                return {"message": "Item already in compare"}, 400

        item_data = vehicle_json([vehicle])[0]
        session['compare'].append(item_data)
        session.modified = True
        return item_data, 200
    else:
        return {"message": "No vehicle to add"}, 400