from ...models.vehicle import Vehicle
from ...extensions import db
from datetime import datetime

def create_vehicle(
    price,
    discount,
    year,
    make,
    model,
    trim,
    colour,
    type,
    kilometres,
    max_range,
    description,
    date_added=None,
    history=None  # Add history as an optional parameter
):
    if date_added is None:
        date_added = datetime.now().strftime("%F-%R")
    if history is None:
        history = "Default history"  # Provide a default value

    new_vehicle = Vehicle(
        price=price,
        discount=discount,
        year=year,
        make=make,
        model=model,
        trim=trim,
        colour=colour,
        type=type,
        kilometres=kilometres,
        max_range=max_range,
        description=description,
        date_added=date_added,
        history=history  # Include history
    )
    db.session.add(new_vehicle)
    db.session.commit()
    return {"message": f"User '{new_vehicle.id}' created successfully"}, 200
