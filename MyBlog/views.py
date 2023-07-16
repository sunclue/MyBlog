from flask import render_template,request,url_for,redirect,flash

from MyBlog import app,db
from MyBlog.models import Message

@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        name=request.form['name']
        message=request.form['message']
        if not name or not message or len(name)>20 or len(message)>256:
            flash('输入错误！')
            return redirect(url_for('index'))
        amessage=Message(name=name,message=message)
        db.session.add(amessage)
        db.session.commit()
        flash('留言成功')
        return redirect(url_for('index'))

    return render_template('index.html')

@app.route('/message',methods=['GET','POST'])
def message():
    if request.method=='POST':
        name=request.form['name']
        message=request.form['message']
        if not name or not message or len(name)>20 or len(message)>256:
            flash('输入错误！')
            return redirect(url_for('message'))
        amessage=Message(name=name,message=message)
        db.session.add(amessage)
        db.session.commit()
        flash('留言成功')
        return redirect(url_for('message'))

    messages=Message.query.order_by(Message.id.desc()).all()
    return render_template('message.html',messages=messages)