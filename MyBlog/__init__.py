import os
import sys

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

WIN=sys.platform.startswith('win')
if WIN:
    prefix='sqlite:///'
else :
    prefix='sqlite:////'
ALLOWED_EXTENSIONS = set(['md','pdf'])

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=prefix+os.path.join(os.path.dirname(app.root_path),os.getenv('DATABASE_FILE','data.db'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY']=os.getenv('SECRET_KEY','dev')
app.config['UPLOAD_FOLDER'] = os.getcwd()+'/MyBlog/static/articles'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

db=SQLAlchemy(app)
login_manager=LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    from MyBlog.models import User
    user=User.query.get(int(user_id))
    return user

from MyBlog import views,errors,commands