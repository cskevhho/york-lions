from ...models.vehicle import Vehicle
from ...extensions import db
from ..vehicle.utils import vehicle_json, generate_image_url

def get_all_vehicles(sort=None, descending="true", min_price=None, max_price=None, condition="all", min_year=None, max_year=None, make="all", model="all", trim="all", colour="all", limit=None):
    vehicles = db.session.query(Vehicle).filter(Vehicle.is_for_sale == True)

    desc = descending and descending.lower() == "true"

    if sort:
        if sort == "date_added":
            vehicles = vehicles.order_by(Vehicle.date_added.desc() if desc else Vehicle.date_added)
        elif sort == "price":
            vehicles = vehicles.order_by(Vehicle.total_price.desc() if desc else Vehicle.total_price)
        elif sort == "km":
            vehicles = vehicles.order_by(Vehicle.kilometres.desc() if desc else Vehicle.kilometres)
        elif sort == "year":
            vehicles = vehicles.order_by(Vehicle.year.desc() if desc else Vehicle.year)
        elif sort == "hot_deals":
            vehicles = vehicles.filter(Vehicle.discount > 0).order_by(Vehicle.discount_percentage.desc() if desc else Vehicle.discount_percentage)
        else:
            vehicles = vehicles.order_by(Vehicle.date_added.desc())
    else:
        vehicles = vehicles.order_by(Vehicle.date_added.desc())

    if min_price:
        try:
            min_price = float(min_price)
        except:
            min_price = -1
        finally:
            if min_price > 0:
                vehicles = vehicles.filter(Vehicle.total_price >= min_price)

    if max_price:
        try:
            max_price = float(max_price)
        except:
            max_price = -1
        finally:
            if max_price > 0:
                vehicles = vehicles.filter(Vehicle.total_price <= max_price)

    if condition == "new":
        vehicles = vehicles.filter(Vehicle.kilometres == 0)
    elif condition == "used":
        vehicles = vehicles.filter(Vehicle.kilometres > 0)

    if min_year:
        try:
            min_year = int(min_year)
        except:
            min_year = -1
        finally:
            if min_year > 0:
                vehicles = vehicles.filter(Vehicle.year >= min_year)

    if max_year:
        try:
            max_year = int(max_year)
        except:
            max_year = -1
        finally:
            if max_year > 0:
                vehicles = vehicles.filter(Vehicle.year <= max_year)

    if make and make != "all" and make != "":
        vehicles = vehicles.filter(Vehicle.make == make)
    if model and model != "all" and model != "":
        vehicles = vehicles.filter(Vehicle.model == model)
    if trim and trim != "all" and trim != "":
        vehicles = vehicles.filter(Vehicle.trim == trim)

    if colour and colour != "all" and colour != "":
        vehicles = vehicles.filter(Vehicle.colour == colour)

    if limit:
        vehicles = vehicles.limit(limit).all()
    else:
        vehicles = vehicles.all()
    # TODO: .paginate(page=page, per_page=per_page, error_out=error_out, max_per_page=max_per_page)

    if not vehicles:
        return {"message": "No vehicles found"}, 400
    
    for vehicle in vehicles:
        vehicle.image_file = generate_image_url(vehicle)

    vehicle_data = vehicle_json(vehicles) # note this is will return that json format response thing
    return vehicle_data, 200

def get_models_by_make():
    models_by_make = {} 
    makes = db.session.query(Vehicle.make).distinct().order_by(Vehicle.make)
    for make in makes:
        models = db.session.query(Vehicle.model).filter_by(make=make[0]).distinct().order_by(Vehicle.model).all()
        trims_by_model = {}
        for model in models:
            trims = db.session.query(Vehicle.trim).filter_by(model=model[0]).distinct().order_by(Vehicle.trim).all()
            trims_for_this_model = []
            for trim in trims:
                trims_for_this_model.append(trim[0])
            trims_by_model[model[0]] = trims_for_this_model
        models_by_make[make[0]] = trims_by_model
    print(models_by_make)
    return models_by_make

def get_colours():
    return db.session.query(Vehicle.colour).distinct().order_by(Vehicle.colour).all()