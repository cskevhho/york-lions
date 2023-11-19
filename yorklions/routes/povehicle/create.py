from ...models.povehicle import POVehicle
from ...extensions import db

def create_povehicle(po_id, vehicle_id, price):
    new_povehicle = POVehicle(po_id=po_id,
    vehicle_id=vehicle_id,
    price=price
    )
    db.session.add(new_povehicle)
    db.session.commit()
    return new_povehicle #{"message": f"Purchase Order Vehicle '{new_povehicle.id}' created successfully", "new_povehicle_id": new_povehicle.id}, 200
