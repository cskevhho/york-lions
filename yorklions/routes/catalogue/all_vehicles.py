from ...models.vehicle import Vehicle
from ...extensions import db
from ..vehicle.utils import vehicle_json, generate_image_url

def get_all_vehicles(sort=None, descending="true", min_price=None, max_price=None, condition="all", min_year=None, max_year=None, min_range=None, max_range=None, min_kilometres=None, max_kilometres=None, type="all", make="all", model="all", trim="all", colour="all", limit=None):
    vehicles = db.session.query(Vehicle).filter(Vehicle.is_for_sale == True)

    desc = descending and descending.lower() == "true"

    if sort:
        if sort == "date_added":
            vehicles = vehicles.order_by(Vehicle.date_added.desc() if desc else Vehicle.date_added)
        elif sort == "price":
            vehicles = vehicles.order_by(Vehicle.total_price.desc() if desc else Vehicle.total_price)
        elif sort == "km":
            vehicles = vehicles.order_by(Vehicle.kilometres.desc() if desc else Vehicle.kilometres)
        elif sort == "range":
            vehicles = vehicles.order_by(Vehicle.max_range.desc() if desc else Vehicle.max_range)
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

    if min_range:
        try:
            min_range = int(min_range)
        except:
            min_range = -1
        finally:
            if min_range > 0:
                vehicles = vehicles.filter(Vehicle.max_range >= min_range)
    if max_range:
        try:
            max_range = int(max_range)
        except:
            max_range = -1
        finally:
            if max_range > 0:
                vehicles = vehicles.filter(Vehicle.max_range <= max_range)

    if min_kilometres:
        try:
            min_kilometres = int(min_kilometres)
        except:
            min_kilometres = -1
        finally:
            if min_kilometres > 0:
                vehicles = vehicles.filter(Vehicle.kilometres >= min_kilometres)
    if max_kilometres:
        try:
            max_kilometres = int(max_kilometres)
        except:
            max_kilometres = -1
        finally:
            if max_kilometres > 0:
                vehicles = vehicles.filter(Vehicle.kilometres <= max_kilometres)

    if type and type != "all" and type != "":
        vehicles = vehicles.filter(Vehicle.type == type)

    if make and make != "all" and make != "":
        vehicles = vehicles.filter(Vehicle.make == make)
    if model and model != "all" and model != "":
        vehicles = vehicles.filter(Vehicle.model == model)
    if trim and trim != "all" and trim != "":
        vehicles = vehicles.filter(Vehicle.trim == trim)

    if colour and colour != "all" and colour != "":
        vehicles = vehicles.filter(Vehicle.colour == colour)

    if limit:
        vehicles = vehicles.limit(limit)
    else:
        vehicles = vehicles
    # TODO: .paginate(page=page, per_page=per_page, error_out=error_out, max_per_page=max_per_page)

    types = db.session.query(Vehicle.type).distinct().order_by(Vehicle.type)
    makes = db.session.query(Vehicle.make).distinct().order_by(Vehicle.make)
    models = db.session.query(Vehicle.model).distinct().filter(Vehicle.make == make).order_by(Vehicle.model)
    trims = models.with_entities(Vehicle.trim).distinct().filter(Vehicle.model == model).order_by(Vehicle.trim)
    colours = db.session.query(Vehicle.colour).distinct().order_by(Vehicle.colour)

    vehicles = vehicles.all()
    
    for vehicle in vehicles:
        vehicle.image_file = generate_image_url(vehicle)

    result = {
        "vehicles": vehicle_json(vehicles),
        "types": types.all(),
        "makes": makes.all(),
        "models": models.all(),
        "trims": trims.all(),
        "colours": colours.all()
    }
    return result, 200
