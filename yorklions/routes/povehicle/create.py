from ...models.povehicle import POVehicle
from ...extensions import db

def create_povehicle(vehicle_id, price):
    new_povehicle = POVehicle(id=vehicle_id, price=price)
    db.session.add(new_povehicle)
    db.session.commit()
    return {"message": f"Purchase Order Vehicle '{new_povehicle.id}' created successfully", "new_povehicle_id": new_povehicle.id}, 200
