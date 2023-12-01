from sqlalchemy import Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..extensions import db
from datetime import datetime

class Rating(db.Model):
    __tablename__ = "ratings"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    make: Mapped[str] = mapped_column(String, nullable=False)
    model: Mapped[str] = mapped_column(String, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    f_name: Mapped[str] = mapped_column(String, nullable=True)  # Allow nullable if anonymous ratings are possible
    l_initial: Mapped[str] = mapped_column(String, nullable=True)  # Allow nullable if anonymous ratings are possible
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    review_body: Mapped[str] = mapped_column(String, nullable=True)
    review_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)  # Use DateTime type

