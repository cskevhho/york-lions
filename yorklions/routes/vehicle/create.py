from ...models.vehicle import Vehicle
from ...extensions import db


def create_vehicle(year, make, model, trim, colour, type, kilometres, max_range):
    new_vehicle = Vehicle(year=year, make=make, model=model, trim=trim, colour=colour, type=type, kilometres=kilometres, max_range=max_range)
    db.session.add(new_vehicle)
    db.session.commit()
    return {"message": f"Vehicle '{new_vehicle.id}' created successfully"}, 200
