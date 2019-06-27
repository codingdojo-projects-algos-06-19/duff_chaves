from config import db
from sqlalchemy.sql import func

class Tour(db.Model):
    __tablename__ = 'tours'
    id = db.Column(db.Integer, primary_key=True)
    venue_name = db.Column(db.String(45))
    venue_address = db.Column(db.String(45))
    venue_city = db.Column(db.String(45))
    venue_state = db.Column(db.String(45))
    venue_country = db.Column(db.String(45))
    venue_phone = db.Column(db.String(45))
    event_date = db.Column(db.DateTime) # Have to work this out correctly.
    event_img = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())