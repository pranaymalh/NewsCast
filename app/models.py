from app import db
from werkzeug.security import generate_password_hash,check_password_hash

class User(db.Document):
	user_id=db.IntField(unique=True)
	email=db.StringField(unique=True,max_length=50)
	first_name=db.StringField(max_length=50)
	last_name=db.StringField(max_length=50)
	password=db.StringField(max_length=120)
	def set_password(self,password):
		self.password=generate_password_hash(password)		
	def get_password(self,password):
		return check_password_hash(self.password,password)

class News(db.Document):
	news_id=db.StringField(unique=True)
	headline=db.StringField(max_length=50)
	description=db.StringField(max_length=1000)
	author_name=db.StringField(max_length=50)
	cat_news=db.StringField(max_length=50)