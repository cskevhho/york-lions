from ...models.povehicle import POVehicle
from ...extensions import db

def get_povehicle(id):
    return db.session.query(POVehicle).filter_by(id=id).first()
