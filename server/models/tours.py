from config import db
from sqlalchemy.sql import func

class Tour(db.Model):
    __tablename__ = 'tours'
    id = db.Column(db.Integer, primary_key=True)
    venue_name = db.Column(db.String(45), nullable=False)
    venue_address = db.Column(db.String(45), nullable=False)
    venue_city = db.Column(db.String(45), nullable=False)
    venue_country = db.Column(db.String(45), nullable=False)
    venue_phone = db.Column(db.String(45), nullable=False)
    event_date = db.Column(db.DateTime) # Have to work this out correctly.
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
    # Relationships Below
    # One User to Many Tour
    # fkey_tour_user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False) # Tested and Working
    # fkey_tour_user = db.relationship('User', foreign_keys=['fkey_tour_user_id'], backref="fkey_tour_user_backref", cascade="all") # Tested and Working
    # # One Address to Many Tour
    # fkey_tour_address_id = db.Column(db.Integer, db.ForeignKey('addresses.id'), nullable=False) # Tested and Working
    # fkey_tour_address = db.relationship('Address', foreign_keys=['fkey_tour_address_id'], backref="fkey_tour_address_backref", cascade="all") # Tested and Working
