from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,SelectField,TextAreaField
from wtforms.validators import Email,Length,DataRequired,EqualTo
class LoginForm(FlaskForm):
	email=StringField("Email",validators=[DataRequired(),Email()])
	password=PasswordField("Password",validators=[DataRequired(),Length(min=6,max=20)])
	submit=SubmitField("Login")

	

class RegisterForm(FlaskForm):
	email=StringField("Email",validators=[DataRequired(),Email()])
	password=PasswordField("Password",validators=[DataRequired(),Length(min=6,max=20)])
	password_confirm=PasswordField("Confirm Password",validators=[DataRequired(),Length(min=6,max=20),EqualTo('password')])
	first_name=StringField("First Name",validators=[DataRequired(),Length(min=2,max=55)])
	last_name=StringField("Last Name",validators=[DataRequired(),Length(min=2,max=55)])
	submit=SubmitField("Register")

class AddNewsForm(FlaskForm):
	choices=['Sports','Politics','Entertainment','General','Lifestyle','Travel','Covid','Others']
	headline=StringField("Headline",validators=[DataRequired(),Length(min=5,max=50)])
	description=TextAreaField("Description",validators=[DataRequired(),Length(min=20,max=1000)])
	cat_news=SelectField("Select Category",choices=choices)
	submit=SubmitField("Publish News")