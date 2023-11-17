from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..extensions import db
from typing import List


class VisitEvent(db.Model):
    __tablename__ = "visitevents"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    ipaddress: Mapped[str] = mapped_column(String, nullable=False)
    date: Mapped[str] = mapped_column(String, nullable=False)
    vehicle_id: Mapped[int] = mapped_column(ForeignKey("vehicles.id"), nullable=False)
    eventtype: Mapped[str] = mapped_column(String, nullable=False)