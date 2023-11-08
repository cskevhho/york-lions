from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from ..extensions import db


class Product(db.Model):
    __tablename__ = "products"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    url: Mapped[str] = mapped_column(String, unique=True, nullable=False)