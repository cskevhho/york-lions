from ...models.user import User
from ...models.address import Address
from ...extensions import db
from datetime import datetime

def create_address(street, city, province, postal_code, phone, user):
    new_address = Address(street=street, city=city, province=province, postal_code=postal_code, phone=phone, user=user)
    db.session.add(new_address)
    db.session.commit()
    return {"message": f"Address '{new_address.id}' created successfully", "new_address_id": new_address.id}, 200
