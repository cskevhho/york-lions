from ...models.address import Address
from ...extensions import db

def get_address(id):
    return db.session.query(Address).filter_by(id=id).first()