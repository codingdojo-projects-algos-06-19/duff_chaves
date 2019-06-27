from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.sql import func
from sqlalchemy import inspect
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
import os

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key="super super secret"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///demo_band.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

ROOT_DIR = os.path.dirname(__file__)
TEMPLATE_DIR = os.path.join(ROOT_DIR, 'client', 'templates')
STATIC_DIR = os.path.join(ROOT_DIR, 'client', 'static')

app.template_folder = TEMPLATE_DIR
app.static_folder = STATIC_DIR

db = SQLAlchemy(app)
migrate = Migrate(app, db)