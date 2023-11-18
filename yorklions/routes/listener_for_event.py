from ...extensions import db
from ...models.visitevent import VisitEvent

def addToLog(visitEvent):
    db.session.add(visitEvent)
    db.session.commit()