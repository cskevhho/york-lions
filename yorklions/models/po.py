from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.hybrid import hybrid_property
from ..extensions import db
from typing import List


class PurchaseOrder(db.Model):
    __tablename__ = "purchaseorders"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'), nullable=True)
    fname: Mapped[str] = mapped_column(String, nullable=False)
    lname: Mapped[str] = mapped_column(String, nullable=False)
    status: Mapped[str] = mapped_column(String, nullable=False, default="Pending")
    address_id: Mapped[int] = mapped_column(ForeignKey("addresses.id"), nullable=False)
    vehicles: Mapped[List['Vehicle']] = relationship('Vehicle', back_populates='purchase_order')
    cc_type: Mapped[str] = mapped_column(String, nullable=False)
    cc_last_4_digits: Mapped[str] = mapped_column(String, nullable=False)
    date_created: Mapped[str] = mapped_column(String, nullable=False)
    latest_update: Mapped[str] = mapped_column(String, nullable=False)
    user: Mapped['User'] = relationship('User', back_populates='orders')

    @hybrid_property
    def subtotal(self):
        result = 0
        for vehicle in self.vehicles:
            result += vehicle.price
        return result
    latest_update: Mapped[str] = mapped_column(String, nullable=False)

    @hybrid_property
    def discount(self):
        result = 0
        for vehicle in self.vehicles:
            result += vehicle.discount
        return result
    latest_update: Mapped[str] = mapped_column(String, nullable=False)

    @hybrid_property
    def taxes(self):
        return (self.subtotal - self.discount) * 0.13
    
    @hybrid_property
    def total_paid(self):
        return self.subtotal - self.discount + self.taxes
    