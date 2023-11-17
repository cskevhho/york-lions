from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..extensions import db
from typing import List


class POVehicle(db.Model):
    __tablename__ = "purchaseorder_vehicles"
    id: Mapped[int] = mapped_column(ForeignKey("purchaseorders.id"), primary_key=True)
    vehicle_id: Mapped[int] = mapped_column(ForeignKey("vehicles.id"), primary_key=True)
    price: Mapped[float] = mapped_column(Integer, primary_key=False)