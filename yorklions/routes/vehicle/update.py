from ...models.vehicle import Vehicle
from ...extensions import db


def update_vehicle(id, updated_data):
    vehicle = Vehicle.query.get(id)
    if not vehicle:
        return {"message": f"Vehicle with ID {id} not found"}, 404

    vehicle.price = updated_data.get("price", vehicle.price)
    vehicle.year = updated_data.get("year", vehicle.year)
    vehicle.make = updated_data.get("make", vehicle.make)
    vehicle.model = updated_data.get("model", vehicle.model)
    vehicle.trim = updated_data.get("trim", vehicle.trim)
    vehicle.colour = updated_data.get("colour", vehicle.colour)
    vehicle.type = updated_data.get("type", vehicle.type)
    vehicle.kilometres = updated_data.get("kilometres", vehicle.kilometres)
    vehicle.max_range = updated_data.get("max_range", vehicle.max_range)
    vehicle.description = updated_data.get("description", vehicle.description)

    db.session.commit()
    return {"message": f"Vehicle '{vehicle.id}' updated successfully"}, 200
