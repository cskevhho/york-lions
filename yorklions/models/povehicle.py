from sqlalchemy import Integer, String, ForeignKey, UniqueConstraint, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..extensions import db
from typing import List


class POVehicle(db.Model):
    __tablename__ = "purchaseorder_vehicles"
    __table_args__ = {'extend_existing': True}
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    po_id: Mapped[int] = mapped_column(Integer, ForeignKey('purchaseorders.id'), nullable=False)
    vehicle_id: Mapped[int] = mapped_column(Integer, ForeignKey('vehicles.id'), nullable=False)
    purchase_orders: Mapped['PurchaseOrder'] = relationship('PurchaseOrder', back_populates='vehicles')
    vehicle: Mapped['Vehicle'] = relationship('Vehicle', back_populates='purchase_orders')
    price: Mapped[float] = mapped_column(Float)