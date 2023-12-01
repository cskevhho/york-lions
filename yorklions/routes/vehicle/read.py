from ...models.vehicle import Vehicle
from ...models.rating import Rating
from ...extensions import db
from ..vehicle.utils import vehicle_json
from sqlalchemy import func

def get_vehicle(id):
    return db.session.query(Vehicle).filter_by(id=id).first()

def get_vehicle_makes():
    makes = [v.make for v in Vehicle.query.with_entities(Vehicle.make).distinct()]
    return makes

def get_average_rating(selected_make, selected_model, selected_year):
    average_rating = db.session.query(func.avg(Rating.rating)).filter(
        Rating.make == selected_make,
        Rating.model == selected_model,
        Rating.year == selected_year
    ).scalar()

    average_rating = float(average_rating) if average_rating is not None else 0.0
    average_rating = max(0.0, min(average_rating, 5.0))

    return average_rating

def read_vehicles(request):
    search_type = request.form['search_type']
    search_text = request.form['search_field']

    if search_type == "vehicle_id":
        vehicles = db.session.query(Vehicle).filter_by(id=search_text).all()
    elif search_type == "price":
        vehicles = db.session.query(Vehicle).filter_by(price=search_text).all()
    elif search_type == "discount":
        vehicles = db.session.query(Vehicle).filter_by(discount=search_text).all()
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
    elif search_type == "date_added":
        vehicles = db.session.query(Vehicle).filter_by(date_added=search_text).all()
    else:
        vehicles = db.session.query(Vehicle).all()

    if not vehicles:
        return {"message": "No vehicles found"}, 400

    vehicle_data = vehicle_json(vehicles) # note this is will return that json format response thing
    return {"vehicles": vehicle_data}, 200
