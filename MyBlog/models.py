import time

from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

from MyBlog import db

class Message(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(20))
    message=db.Column(db.String(256))

class User(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(20))
    username=db.Column(db.String(20))
    password_hash=db.Column(db.String(128))

    def set_password(self,password):
        self.password_hash=generate_password_hash(password)

    def validate_password(self,password):
        return check_password_hash(self.password_hash,password)
    
class Article(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(64))
    description=db.Column(db.String(512))
    date=db.Column(db.String(12))
    category=db.Column(db.String(16))

    def set_date(self):
        self.date=time.strftime('%Y-%m-%d', time.localtime())