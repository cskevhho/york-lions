from ...models.trade_in import TradeIn

def trade_in_json(trade_ins: list[TradeIn]):
    trade_in_data = [
        {
            "id": trade_in.id,
            "user_id": trade_in.user_id,
            "vehicle_id": trade_in.vehicle_id,
            "status": trade_in.status,
            "quote": trade_in.quote,
            "accidents": trade_in.accidents,
            "details": trade_in.details,
            "date_updated": trade_in.date_updated,
        }
        for trade_in in trade_ins
    ]
    return trade_in_data