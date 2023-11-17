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
    user_id,
    date_added=None,
):
    if date_added is None:
        date_added = datetime.now().strftime("%F-%R")
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
        user_id=user_id,
        date_added=date_added,
    )
    db.session.add(new_vehicle)
    db.session.commit()
    return {"message": f"User '{new_vehicle.id}' created successfully"}, 200
