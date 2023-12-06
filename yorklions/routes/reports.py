from ...models.visitevent import VisitEvent
from ...models.po import PurchaseOrder
from ...extensions import db
from flask import Flask, request, render_template, session

@app.route('/get-sales-report', methods=['GET', 'POST'])
def generate_sales_report():
    if descending == "true":
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
    return render_template('admin.html', salesReport_des=salesReport_des), 200

@app.route('/get-usage-report', methods=['GET', 'POST'])
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
    return render_template('admin.html', eventReport=eventReport), 200
