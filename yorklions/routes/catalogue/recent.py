from ...models.vehicle import Vehicle
from ...extensions import db

def recent_vehicles(descending=True):

    if descending:
        vehicles = db.session.query(Vehicle).order_by(Vehicle.date_added.desc()).all()
        # TODO: .paginate(page=page, per_page=per_page, error_out=error_out, max_per_page=max_per_page)
    else:
        vehicles = db.session.query(Vehicle).order_by(Vehicle.date_added).all()
        # TODO: .paginate(page=page, per_page=per_page, error_out=error_out, max_per_page=max_per_page)

    if not vehicles:
        return {"message": "No vehicles found"}, 400

    vehicle_data = [
        {
            "id": vehicle.id,
            "price": vehicle.price,
            "year": vehicle.year,
            "make": vehicle.make,
            "model": vehicle.model,
            "trim": vehicle.trim,
            "colour": vehicle.colour,
            "type": vehicle.type,
            "kilometres": vehicle.kilometres,
            "max_range": vehicle.max_range,
            "description": vehicle.description,
            "date_added": vehicle.date_added
        }
        for vehicle in vehicles
    ]  # note this is will return that json format response thing
    return vehicle_data, 200
