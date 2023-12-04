from ...models.vehicle import Vehicle
from ...models.rating import Rating
from ...extensions import db
from flask import request, jsonify


def get_ratings(vehicle: Vehicle):
    return db.session.query(Rating).filter_by(year=vehicle.year).filter_by(make=vehicle.make).filter_by(model=vehicle.model).all()


def admin_get_ratings(request):
    ratings = db.session.query(Rating).all()
    # set id to _id to keep id at the top of the json object
    rating_list = [{'_id': rating.id, 'year': rating.year, 'make': rating.make, 'model': rating.model, 'first name': rating.f_name, 'last initial': rating.l_initial } for rating in ratings]
    return jsonify(rating_list)

