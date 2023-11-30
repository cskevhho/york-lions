from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..extensions import db


# We're going to assume only Canadian addressses for now
class Address(db.Model):
    __tablename__ = "addresses"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    street: Mapped[str] = mapped_column(String, nullable=False)
    city: Mapped[str] = mapped_column(String, nullable=False)
    province: Mapped[str] = mapped_column(String(2), nullable=False)
    postal_code: Mapped[str] = mapped_column(String(6), nullable=False)
    phone: Mapped[str] = mapped_column(String)
    user: Mapped["User"] = relationship("User", back_populates="address")