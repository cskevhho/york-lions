from ...models.po import PurchaseOrder
from ...extensions import db

def get_po(id):
    return db.session.query(PurchaseOrder).filter_by(id=id).first()