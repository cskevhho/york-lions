from ...models.trade_in import TradeIn
from ...extensions import db


def delete_all():
    trade_ins = TradeIn.query.all()

    if not TradeIn.query.all():
        return {"message": "No trade-ins to delete"}, 400
    for trade_in in trade_ins:
        db.session.delete(trade_in)

    db.session.commit()
    return {"message": "All trade-ins deleted successfully"}, 200
