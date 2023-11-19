from ...models.visitevent import VisitEvent
from ...models.po import PurchaseOrder
from ...extensions import db

def generate_sales_report(descending=True):
    if descending:
        sales = db.session.query(PurchaseOrder).order_by(PurchaseOrder.date.desc()).all()
    else:
        sales = db.session.query(PurchaseOrder).order_by(PurchaseOrder.date).all()
    salesReport = [
        {
            "id": po.id,
            "fnmae": po.fname,
            "lname": po.lname,
            "status": po.ststus,
            "address id": po.address_id,
            "purchase orders": po.purchase_orders,
            "date": po.date 
        }
        for po in sales
    ]
    return salesReport, 200
    #I'll figure out the spreadsheet thing later

def generate_app_usage():
    events = db.session.query(VisitEvent).order_by(VisitEvent.date.desc()).all()
    eventReport = [
        {
            "id": visitevents.id,
            "ipaddress": visitevents.ipaddress,
            "date": visitevents.date,
            "vehicle_id": visitevents.vehicle_id,
            "event_type": visitevents.eventtype
        }
        for visitevents in events
    ] #add the listeners
    return eventReport, 200
