from ...models.vehicle import Vehicle
from ...extensions import db
from ..vehicle.utils import vehicle_json, generate_image_url

def get_recent_vehicles(limit=None, descending=True):

    if descending:
        if limit:
            vehicles = db.session.query(Vehicle).filter(Vehicle.is_for_sale == True).order_by(Vehicle.date_added.desc()).limit(limit).all()
        else:
            vehicles = db.session.query(Vehicle).filter(Vehicle.is_for_sale == True).order_by(Vehicle.date_added.desc()).all()
        # TODO: .paginate(page=page, per_page=per_page, error_out=error_out, max_per_page=max_per_page)
    else:
        if limit:
            vehicles = db.session.query(Vehicle).filter(Vehicle.is_for_sale == True).order_by(Vehicle.date_added).limit(limit).all()
        else:
            vehicles = db.session.query(Vehicle).filter(Vehicle.is_for_sale == True).order_by(Vehicle.date_added).all()
        # TODO: .paginate(page=page, per_page=per_page, error_out=error_out, max_per_page=max_per_page)

    if not vehicles:
        return {"message": "No vehicles found"}, 400
    
    for vehicle in vehicles:
        vehicle.image_file = generate_image_url(vehicle)

    vehicle_data = vehicle_json(vehicles) # note this is will return that json format response thing
    return vehicle_data, 200
