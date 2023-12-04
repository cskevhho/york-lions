from ...models.trade_in import TradeIn
from ...extensions import db


def update_trade_in(id, updated_data):
    trade_in = TradeIn.query.get(id)
    if not trade_in:
        return {"message": f"Trade-In with ID {id} not found"}, 404

    trade_in.id = updated_data.get("id", trade_in.id)
    
    new_value = updated_data.get("user_id")
    if new_value and new_value != "":
        trade_in.user_id = updated_data.get("user_id", trade_in.user_id)

    new_value = updated_data.get("vehicle_id")
    if new_value and new_value != "":
        trade_in.vehicle_id = updated_data.get("vehicle_id", trade_in.vehicle_id)

    new_value = updated_data.get("status")
    if new_value and new_value != "":
        trade_in.status = updated_data.get("status", trade_in.status)

    new_value = updated_data.get("quote")
    if new_value and new_value != "":
        trade_in.quote = updated_data.get("quote", trade_in.quote)

    new_value = updated_data.get("accidents")
    if new_value and new_value != "":
        trade_in.accidents = updated_data.get("accidents", trade_in.accidents)

    new_value = updated_data.get("details")
    if new_value and new_value != "":
        trade_in.details = updated_data.get("details", trade_in.details)

    new_value = updated_data.get("date_updated")
    if new_value and new_value != "":
        trade_in.date_updated = updated_data.get("date_updated", trade_in.date_updated)

    db.session.commit()
    return {"message": f"Trade-In '{trade_in.id}' updated successfully"}, 200
