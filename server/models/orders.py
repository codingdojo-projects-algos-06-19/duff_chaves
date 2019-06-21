from config import db
from sqlalchemy.sql import func
from server.models.users import User
from server.models.addresses import Address
from server.models.items import Item
from server.models.orders_items import orders_items

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
    # Relationships Below
    # Many to Many / Order and Item
    items_for_orders = db.relationship('Item', secondary=orders_items) # Tested and Working
    # One User to Many Order
    fkey_order_user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False) # Tested and Working
    fkey_order_user = db.relationship('User', foreign_keys=['fkey_order_user_id'], backref="fkey_order_user_backref", cascade="all") # Tested and Working
    #One Address to Many Order
    fkey_order_address_id = db.Column(db.Integer, db.ForeignKey('addresses.id'), nullable=False) # Tested and Working
    fkey_order_address = db.relationship('Address', foreign_keys=['fkey_order_address_id'], backref="fkey_order_address_backref", cascade="all") # Tested and Working
