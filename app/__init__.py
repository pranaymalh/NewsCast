from flask import Flask
from config import Config
from flask_mongoengine import MongoEngine
from flask_restplus import Api
app=Flask(__name__)
api=Api()
app.config.from_object(Config)
db=MongoEngine()
db.init_app(app)
api.init_app(app)
app.static_folder = 'static'
from app import routes