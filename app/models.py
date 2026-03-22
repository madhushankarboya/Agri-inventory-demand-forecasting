from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(120))
    password = db.Column(db.String(200))
 role = db.Column(db.String(50), default="Farmer")  # Admin / Officer / Data Analyst / Public
    approved = db.Column(db.Boolean, default=False)
    deault_role = "Public User"
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
