from config import db
from sqlalchemy.sql import func
from server.models.users import User
from server.models.orders import Order
from server.models.orders_items import orders_items

class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(45), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
    # Relationships Below
    # Many to Many / Order and Item
    orders_for_items = db.relationship('Order', secondary=orders_items) # Tested and Working
    # One User to Many Item
    fkey_item_user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False) # Tested and Working
    fkey_item_user = db.relationship('User', foreign_keys=['fkey_item_user_id'], backref="fkey_item_user_backref", cascade="all") # Tested and Working

