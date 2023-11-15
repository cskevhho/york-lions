from ...models.vehicle import Vehicle
from ...extensions import db


def read_vehicle(request):
    search_type = request.form['search_type']
    search_text = request.form['search_field']

    if search_type == "vehicle_id":
        vehicles = db.session.query(Vehicle).filter_by(id=search_text).all()
    elif search_type == "price":
        vehicles = db.session.query(Vehicle).filter_by(price=search_text).all()
    elif search_type == "year":
        vehicles = db.session.query(Vehicle).filter_by(year=search_text).all()
    elif search_type == "make":
        vehicles = db.session.query(Vehicle).filter_by(make=search_text).all()
    elif search_type == "model":
        vehicles = db.session.query(Vehicle).filter_by(model=search_text).all()
    elif search_type == "trim":
        vehicles = db.session.query(Vehicle).filter_by(trim=search_text).all()
    elif search_type == "colour":
        vehicles = db.session.query(Vehicle).filter_by(colour=search_text).all()
    elif search_type == "type":
        vehicles = db.session.query(Vehicle).filter_by(type=search_text).all()
    elif search_type == "kilometres":
        vehicles = db.session.query(Vehicle).filter_by(kilometres=search_text).all()
    elif search_type == "max_range":
        vehicles = db.session.query(Vehicle).filter_by(max_range=search_text).all()
    elif search_type == "description":
        vehicles = db.session.query(Vehicle).filter_by(description=search_text).all()
    else:
        vehicles = db.session.query(Vehicle).all()

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
            "description": vehicle.description
        }
        for vehicle in vehicles
    ]  # note this is will return that json format response thing
    return {"vehicles": vehicle_data}, 200
