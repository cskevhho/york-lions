from ...models.trade_in import TradeIn
from ...extensions import db
from ..trade_in.utils import trade_in_json

def read_trade_ins(request):
    search_type = request.form['search_type']
    search_text = request.form['search_field']

    if search_type == "trade_in_id":
        trade_ins = db.session.query(TradeIn).filter_by(id=search_text).all()
    else:
        trade_ins = db.session.query(TradeIn).all()

    if not trade_ins:
        return {"message": "No trade-ins found"}, 400

    trade_in_data = trade_in_json(trade_ins) # note this is will return that json format response thing
    return {"trade_ins": trade_in_data}, 200

def get_trade_in(id):
    return db.session.query(TradeIn).filter_by(id=id).first()
