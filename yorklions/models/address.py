from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from ..extensions import db
from .user import User

# We're going to assume only Canadian addressses for now
class Address(db.Model):
    __tablename__ = "addresses"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    street: Mapped[str] = mapped_column(String, nullable=False)
    city: Mapped[str] = mapped_column(String, nullable=False)
    province: Mapped[str] = mapped_column(String(2), nullable=False)
    zipcode: Mapped[str] = mapped_column(String(6), nullable=False)
    phone: Mapped[str] = mapped_column(String, nullable=False)
    user_id: Mapped[int] = mapped_column(
        Integer, db.ForeignKey("users.id"), nullable=False
    )
