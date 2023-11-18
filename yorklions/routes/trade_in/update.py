from ...models.trade_in import TradeIn
from ...extensions import db


def update_trade_in(id, updated_data):
    trade_in = TradeIn.query.get(id)
    if not trade_in:
        return {"message": f"Trade-In with ID {id} not found"}, 404


    trade_in.id = updated_data.get("id", trade_in.id)
    trade_in.user_id = updated_data.get("user_id", trade_in.user_id)
    trade_in.vehicle_id = updated_data.get("vehicle_id", trade_in.vehicle_id)
    trade_in.status = updated_data.get("status", trade_in.status)
    trade_in.quote = updated_data.get("quote", trade_in.quote)
    trade_in.accidents = updated_data.get("accidents", trade_in.accidents)
    trade_in.details = updated_data.get("details", trade_in.details)
    trade_in.date_updated = updated_data.get("date_updated", trade_in.date_updated)

    db.session.commit()
    return {"message": f"Trade-In '{trade_in.id}' updated successfully"}, 200
