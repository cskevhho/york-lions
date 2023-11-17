from sqlalchemy import Integer, Float, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.ext.hybrid import hybrid_property
from ..extensions import db


class Vehicle(db.Model):
    __tablename__ = "vehicles"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    price: Mapped[float] = mapped_column(Float, primary_key=False)
    discount: Mapped[float] = mapped_column(Float, primary_key=False)
    year: Mapped[int] = mapped_column(Integer, primary_key=False)
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

    @hybrid_property
    def discount_percentage(self):
        return 100 * self.discount / self.price
    