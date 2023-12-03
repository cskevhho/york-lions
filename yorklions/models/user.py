from sqlalchemy import Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..extensions import db, login_manager
from flask_login import UserMixin  # adds login_manager required methods
from typing import List

@login_manager.user_loader  # login_managers needs to know how to load a user
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
    is_admin: Mapped[bool] = mapped_column(Boolean, default=False)
    is_guest: Mapped[bool] = mapped_column(Boolean, default=False)
    image_file: Mapped[str] = mapped_column(String, nullable=False, default="default.jpg")
    address_id: Mapped[int] = mapped_column(Integer, ForeignKey('addresses.id'), nullable=True)
    address: Mapped["Address"] = relationship("Address", back_populates="user")
    trade_ins = relationship('TradeIn', backref='user', lazy=True)
    orders: Mapped[List['PurchaseOrder']] = relationship('PurchaseOrder', back_populates='user')
    