from ...extensions import db
from ...models.visitevent import VisitEvent

def addToLog(visitEvent):
    db.session.add(visitEvent)
    db.session.commit()

def createVisitEvent(id, ipaddress, vechile_id, eventtype):
    new_event = VisitEvent(ip=id, ipaddress=ipaddress, date=datetime.now().strftime("%F-%R"), vechile_id=vechile_id, eventtype=eventtype)
    return new_event
