from config import db


# This table is tested and working.
# Many to Many / User and KART and Item
users_cart_items = db.Table('users_cart_items',
                        db.Column('user_id', db.Integer,
                                  db.ForeignKey('users.id'),
                                  primary_key=True),
                        db.Column('item_id', db.Integer,
                                  db.ForeignKey('items.id'),
                                  primary_key=True))