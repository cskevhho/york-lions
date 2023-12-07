from .utils import generate_image_url, vehicle_json
from .read import get_vehicle
from ...wtform.vehicle_forms import CreateVehicleForm
from ...models.vehicle import Vehicle
from ...extensions import db
from datetime import datetime
from flask import request, current_app
from PIL import Image
import secrets, os


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
    is_for_sale=True,
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
        is_for_sale=is_for_sale,
        history=history  # Include history
    )
    db.session.add(new_vehicle)
    db.session.commit()
    return {"message": f"Vehicle '{new_vehicle.id}' created successfully", "new_vehicle_id": new_vehicle.id}, 200


def create_vehicle_from_form(form: CreateVehicleForm):
    print("got here")

    if request.method == "POST":
        price = form.price.data
        discount = form.discount.data or 0
        year = form.year.data
        make = form.make.data
        model = form.model.data
        trim = form.trim.data
        colour = form.colour.data
        type = form.type.data
        kilometres = form.kilometres.data
        max_range = form.max_range.data
        description = form.description.data
        print("got here")
        
        response = create_vehicle(
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
            is_for_sale=True,
        )

        vehicle_id = int(response[0]["new_vehicle_id"])


        pic_file = save_picture(form.picture.data)
        vehicle = get_vehicle(vehicle_id)
        vehicle.image_file = pic_file

        db.session.commit()

        print("got here")

        return vehicle_json([vehicle]), 200
    return {"message": "OK"}, 200

# takes in image, saves it, creates a hex name for it, returns the name of the file
def save_picture(form_pic):
    rand_hex = secrets.token_hex(8)
    if form_pic:
        _, file_ext = os.path.splitext(form_pic.filename) # _ is an unused var name since we're only using the extension?
        pic_filename = rand_hex + file_ext
    else:
        pic_filename = "default.jpg"
    pic_path = os.path.join(current_app.root_path, "static/vehicles", pic_filename)
    
    if form_pic:
        img = Image.open(form_pic)
        img.save(pic_path)
    
    return pic_filename