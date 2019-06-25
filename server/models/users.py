from flask import session
from config import db, bcrypt
from sqlalchemy.sql import func
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(45), nullable=False)
    last_name = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    approval_id = db.Column(db.Integer, server_default='1')
    address1 = db.Column(db.String(255))
    address2 = db.Column(db.String(255))
    city = db.Column(db.String(100))
    state = db.Column(db.String(100))
    country = db.Column(db.String(100))
    postal_code = db.Column(db.String(25))
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

    @classmethod
    def validate(cls, form):
        alerts = []
        get_user_by_email = User.query.filter_by(email=form['email']).first()
        if get_user_by_email != None:
            alerts.append('This email address already exists! Please use a different one.')  

        if len(form['fname']) < 1:
            alerts.append('The first name field is required!')
        elif form['fname'].isalpha() != True:
            alerts.append('Only letters are allowed in the first name field!')

        if len(form['lname']) < 1:
            alerts.append('The last name field is required!')
        elif form['lname'].isalpha() != True:
            alerts.append('Only letters are allowed in the last name field!')
            
        if len(form['email']) < 1:
            alerts.append('The email address field is required!')
        elif not EMAIL_REGEX.match(form['email']):
            alerts.append('Invalid email address!')

        if len(form['address1']) < 1:
            alerts.append('The address one field is required!')

        if len(form['city']) < 1:
            alerts.append('The city field is required!')

        if len(form['state']) < 1:
            alerts.append('The state field is required!')

        if len(form['country']) < 1:
            alerts.append('The country field is required!')

        if len(form['postal_code']) < 1:
            alerts.append('The postal code field is required!')

        if len(form['password']) < 1:
            alerts.append('The password cannot be blank!')
        elif len(form['password']) < 8:
            alerts.append('The password needs to be at least 8 characters')
        elif not re.match(r"^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[@#$])[\w\d@#$]{6,12}$", form['password']):
            alerts.append('The confirmed password must contain a number, a special character, upper and lowercase!')

        if len(form['password2']) < 1:
            alerts.append('The confirmed password cannot be blank!')

        if form['password'] != form['password2']:
            alerts.append('Both passwords should match')
        return alerts

    @classmethod
    def create(cls, form):
        print(form)
        #@A1aaaaa
        pw_hash = bcrypt.generate_password_hash(form['password']) 
        new_user = cls(
            first_name = form['fname'],
            last_name = form['lname'],
            email = form['email'],
            address1 = form['address1'],
            address2 = form['address2'],
            city = form['city'],
            state = form['state'],
            country = form['country'],
            postal_code = form['postal_code'],
            password = pw_hash
        )
        db.session.add(new_user)
        db.session.commit()
        return new_user.id

    @classmethod
    def login_helper(cls, form):
        user = cls.query.filter_by(email=form['email']).first()
        if user:
            if bcrypt.check_password_hash(user.pw_hash, form['password']):
                return (True, user.id)
        return (False, "Email or password incorrect.")