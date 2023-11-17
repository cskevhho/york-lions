from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..extensions import db
from typing import List


class PurchaseOrder(db.Model):
    __tablename__ = "purchaseorders"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fname: Mapped[str] = mapped_column(String, nullable=False)
    lname: Mapped[str] = mapped_column(String, nullable=False)
    status: Mapped[str] = mapped_column(String, nullable=False)
    address_id: Mapped[int] = mapped_column(ForeignKey("addresses.id"), nullable=False)
    product_orders: Mapped[List["POItem"]] = relationship()
