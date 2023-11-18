from sqlalchemy import Integer, Float, String, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.hybrid import hybrid_property
from ..extensions import db
from typing import List

# If you edit this model, update `services.trade_in_json()`

class TradeIn(db.Model):
    __tablename__ = "trade_ins"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'), nullable=False)
    vehicle_id: Mapped[int] = mapped_column(ForeignKey("vehicles.id"))
    status: Mapped[float] = mapped_column(String, primary_key=False, default="Pending Review")
    quote: Mapped[float] = mapped_column(Float, primary_key=False)
    accidents: Mapped[str] = mapped_column(String, nullable=False)
    details: Mapped[str] = mapped_column(String, nullable=False)
    date_updated: Mapped[str] = mapped_column(String, nullable=False)
