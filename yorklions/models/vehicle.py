from sqlalchemy import Integer, Float, String, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.hybrid import hybrid_property
from ..extensions import db
from typing import List
from datetime import datetime

# If you edit this model, update `services.vehicle_json()`

class Vehicle(db.Model):
    __tablename__ = "vehicles"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    po_id: Mapped[int] = mapped_column(Integer, ForeignKey('purchaseorders.id'), nullable=True)
    price: Mapped[float] = mapped_column(Float, primary_key=False)
    discount: Mapped[float] = mapped_column(Float, primary_key=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    make: Mapped[str] = mapped_column(String, nullable=False)
    model: Mapped[str] = mapped_column(String, nullable=False)
    trim: Mapped[str] = mapped_column(String, nullable=False)
    colour: Mapped[str] = mapped_column(String, nullable=False)
    type: Mapped[str] = mapped_column(String, nullable=False)
    kilometres: Mapped[int] = mapped_column(Integer, primary_key=False)
    max_range: Mapped[int] = mapped_column(Integer, primary_key=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    image_file: Mapped[str] = mapped_column(String, nullable=False, default="default.jpg")
    date_added: Mapped[str] = mapped_column(String, nullable=False)
    is_for_sale: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    is_trade_in: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    history: Mapped[List[str]] = mapped_column(String, nullable=True)
    visit_events: Mapped[List["VisitEvent"]] = relationship()
    purchase_order: Mapped['PurchaseOrder'] = relationship('PurchaseOrder', back_populates='vehicles')

    @hybrid_property
    def discount_percentage(self):
        return (100 * self.discount / self.price) if self.price != 0 else 0
    
    @hybrid_property
    def total_price(self):
        return self.price - self.discount
    
