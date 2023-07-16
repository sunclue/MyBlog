import os
import sys

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

WIN=sys.platform.startswith('win')
if WIN:
    prefix='sqlite:///'
else :
    prefix='sqlite:////'

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=prefix+os.path.join(os.path.dirname(app.root_path),os.getenv('DATABASE_FILE','data.db'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY']=os.getenv('SECRET_KEY','dev')

db=SQLAlchemy(app)

from MyBlog import views,errors,commands