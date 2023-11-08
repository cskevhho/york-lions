from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from ..extensions import db


class User(db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True, nullable=False)
