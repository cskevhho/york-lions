from ...models.vehicle import Vehicle
from ...models.po import PurchaseOrder
from ...extensions import db
from datetime import datetime
from flask_login import current_user


def create_po(
    fname: str,
    lname: str,
    address_id: int,
    vehicles: [Vehicle],
    cc_type: str,
    cc_last_4_digits: str
):
    now: str = datetime.now().strftime("%F-%R")
    new_po = PurchaseOrder(
        fname=fname,
        lname=lname,
        address_id=address_id,
        cc_type=cc_type,
        cc_last_4_digits=cc_last_4_digits,
        date_created=now,
        latest_update=now
    )
    new_po.user=current_user
    db.session.add(new_po)
    db.session.commit()

    for vehicle in vehicles:
        new_po.vehicles.append(vehicle)

    db.session.commit()

    return {
        "message": f"Purchase Order '{new_po.id}' created successfully",
        "new_po_id": new_po.id,
    }, 200