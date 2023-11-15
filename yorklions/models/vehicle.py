from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from ..extensions import db


class Vehicle(db.Model):
    __tablename__ = "vehicles"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    year: Mapped[int] = mapped_column(Integer, primary_key=False)
    make: Mapped[str] = mapped_column(String, nullable=False)
    model: Mapped[str] = mapped_column(String, nullable=False)
    trim: Mapped[str] = mapped_column(String, nullable=False)
    colour: Mapped[str] = mapped_column(String, nullable=False)
    type: Mapped[str] = mapped_column(String, nullable=False)
    kilometres: Mapped[int] = mapped_column(Integer, primary_key=False)
    max_range: Mapped[int] = mapped_column(Integer, primary_key=False)
