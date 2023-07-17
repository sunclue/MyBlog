import markdown
import os

from flask import render_template,request,url_for,redirect,flash,Markup

from MyBlog import app,db
from MyBlog.models import Message,User,Article
from flask_login import login_user,login_required,logout_user

def md2html(filename):
	
	exts = ['markdown.extensions.extra', 'markdown.extensions.codehilite','markdown.extensions.tables','markdown.extensions.toc']
	mdcontent = ""
	with open(filename,'r',encoding='utf-8') as f:
		mdcontent = f.read()
		pass	
	html = markdown.markdown(mdcontent,extensions=exts)
	content = Markup(html)
	return content

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

    articles=Article.query.order_by(Article.id.desc()).all()
    return render_template('index.html',articles=articles)

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

@app.route('/blog')
def blog():
    if request.method=='GET':
        id=request.args.get('id')
        if id:
            filename=Article.query.get(id).title+".md"
            path=app.config['UPLOAD_FOLDER']+'/'+filename
            content=md2html(path)
            return render_template('readblog.html',content=content)
    articles=Article.query.order_by(Article.id.desc()).all()
    return render_template('blog.html',articles=articles)

@app.route('/publish',methods=['GET','POST'])
@login_required
def publish():
    if request.method=='POST':
        file=request.files['file']
        if file!='':
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],file.filename))
            title=file.filename.rsplit('.',1)[0]
            description=''
            category=''
            article=Article(title=title,description=description,category=category)
            article.set_date()
            db.session.add(article)
            db.session.commit()
            flash('发表成功！')
            return redirect(url_for('publish'))

    return render_template('publish.html')

@app.route('/adminloginwhichonlyhandsomemanreadonly',methods=['GET','POST'])
def adminlogin():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']

        if not username or not password:
            flash('Invalid input!')
            return redirect(url_for('adminlogin'))
        
        user=User.query.first()
        if user.username==username and user.validate_password(password):
            login_user(user)
            flash('Login success.')
            return redirect(url_for('index'))
        
        flash('Invalid username or password.')
        return redirect(url_for('adminlogin'))
    
    return render_template('adminlogin.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Goodbye!')
    return redirect(url_for('index'))