from ...models.povehicle import POVehicle
from ...extensions import db

def get_povehicle(id):
    return db.session.query(POVehicle).filter_by(id=id).first()

def get_povehicle_by_po_id(po_id):
    return db.session.query(POVehicle).filter_by(po_id=po_id).first()