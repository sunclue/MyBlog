from flask import render_template,request,url_for,redirect,flash

from MyBlog import app

@app.route('/')
def index():
    return render_template('index.html')