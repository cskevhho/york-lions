from ...models.po import PurchaseOrder
from ...extensions import db
from datetime import datetime
from ..povehicle.create import create_povehicle


def create_po(
    fname,
    lname,
    address_id,
    vehicles,
    status="New",
):
    new_po = PurchaseOrder(
        fname=fname,
        lname=lname,
        address_id=address_id,
        status=status,
        date=datetime.now().strftime("%F-%R"),
    )
    db.session.add(new_po)
    db.session.commit()

    for vehicle in vehicles:
        povehicle = create_povehicle(new_po.id, vehicle.id, vehicle.price)
        new_po.vehicles.append(povehicle)

    db.session.commit()

    return {
        "message": f"Purchase Order '{new_po.id}' created successfully",
        "new_po_id": new_po.id,
    }, 200