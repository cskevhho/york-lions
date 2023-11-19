from ...models.vehicle import Vehicle
from flask import url_for

def vehicle_json(vehicles: list[Vehicle]):
    vehicle_data = [
        {
            "id": vehicle.id,
            "price": vehicle.price,
            "discount": vehicle.discount,
            "year": vehicle.year,
            "make": vehicle.make,
            "model": vehicle.model,
            "trim": vehicle.trim,
            "colour": vehicle.colour,
            "type": vehicle.type,
            "kilometres": vehicle.kilometres,
            "max_range": vehicle.max_range,
            "description": vehicle.description,
            "image_file": vehicle.image_file,
            "date_added": vehicle.date_added,
            "history": vehicle.history,
            "visit_events": vehicle.visit_events,
            "product_orders": vehicle.product_orders,
            "discount_percentage": vehicle.discount_percentage,
        }
        for vehicle in vehicles
    ]
    return vehicle_data

def generate_image_url(vehicle):
    return url_for("static", filename="vehicles/" + vehicle.image_file)