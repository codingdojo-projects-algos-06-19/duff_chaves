from config import db

# This table is tested and working.
# Many to Many / Order and Item
orders_items = db.Table('orders_items',
                        db.Column('order_id', db.Integer,
                                  db.ForeignKey('orders.id'),
                                  primary_key=True),
                        db.Column('item_id', db.Integer,
                                  db.ForeignKey('items.id'),
                                  primary_key=True))
