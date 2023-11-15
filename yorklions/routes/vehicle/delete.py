from ...models.vehicle import Vehicle
from ...extensions import db


def delete_all():
    vehicles = Vehicle.query.all()

    if not Vehicle.query.all():
        return {"message": "No vehicles to delete"}, 400
    for vehicle in vehicles:
        db.session.delete(vehicle)

    db.session.commit()
    return {"message": "All vehicles deleted successfully"}, 200
