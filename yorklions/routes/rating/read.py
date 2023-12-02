from ...models.vehicle import Vehicle
from ...models.rating import Rating
from ...extensions import db

def get_ratings(vehicle: Vehicle):
    return db.session.query(Rating).filter_by(year=vehicle.year).filter_by(make=vehicle.make).filter_by(model=vehicle.model).all()
