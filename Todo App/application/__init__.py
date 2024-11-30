from flask import Flask
from flask_pymongo import PyMongo
from application import routes

app = Flask(__name__)
app.config["SECRET_KEY"] = ""
app.config["MONGO_URI"] = ""

# mongodb database
mongodb_client = PyMongo(app)
db = mongodb_client.db

