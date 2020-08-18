from app import app,db,api
from flask import render_template,redirect,url_for,session,flash
from app.forms import LoginForm,RegisterForm,AddNewsForm
from app.models import User,News
from flask_restplus import Resource
import uuid
@app.route("/")
@app.route("/index")
def index():
	return render_template('index.html')

@app.route("/news")
def news():
	classes=News.objects().all()
	return render_template('news.html',classes=classes)

@app.route("/deletenews/<idx>")
def deletenews(idx):
	if News.objects().count()>0:
		News.objects(news_id=idx).delete()
	return redirect(url_for('news'))

@app.route("/addnews",methods=["GET","POST"])
def addnews():
	form=AddNewsForm()
	if form.validate_on_submit():
		id=uuid.uuid4()
		news_id=str(id.int)
		while News.objects(news_id=news_id).first():
			id=uuid.uuid4()
			news_id=str(id.int)
		headline=form.headline.data
		description=form.description.data
		cat_news=form.cat_news.data
		author_name=session.get("username")
		news=News(news_id=news_id,description=description,headline=headline,author_name=author_name,cat_news=cat_news)
		news.save()
		flash(f"News is successfully published!","success")
	return render_template('addnews.html',form=form)

@app.route("/contact")
def contact():
	return render_template('contact.html')

@app.route("/logout",methods=["GET","POST"])
def logout():
	session["user_id"]=False
	session.pop("username",None)
	return redirect(url_for("login"))

@app.route("/login",methods=["GET","POST"])
def login():
	if session.get("username"):
		return redirect(url_for('index'))
	form=LoginForm()
	if form.validate_on_submit():
		email=form.email.data
		password=form.password.data
		user=User.objects(email=email).first()
		if user and user.get_password(password):
			flash(f"{user.first_name}, You are successfully logged in!","success")
			session["user_id"]=user.user_id
			session["username"]=user.first_name
			session["email"]=user.email
			return redirect(url_for('index'))
		flash("Sorry, something went wrong!", "danger")
	return render_template('login.html',form=form)

@app.route("/register",methods=["GET","POST"])
def register():
	if session.get('username'):
		return redirect(url_for('index'))
	form=RegisterForm()
	if form.validate_on_submit():
		user_id=User.objects.count()
		user_id+=1
		email=form.email.data
		if User.objects(email=email).first():
			flash("Email already exists!", "danger")
			return redirect("/register")
		password=form.password.data
		first_name=form.first_name.data
		last_name=form.last_name.data
		user=User(user_id=user_id,email=email,first_name=first_name,last_name=last_name)
		user.set_password(password)
		user.save()
		flash(f"You are successfully registered!","success")
		return redirect(url_for('login'))
	return render_template('register.html',form=form)	