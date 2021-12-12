from flask import Flask
from flask import request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
 

#from vpblog.vpblog import vpblog

app = Flask(__name__)

app.secret_key = 'asl5hkj5k5jg43kjh3kje3nkejndk'
app.config["SESSION_PERMANENT"] = False


app.config["MONGO_URI"] = "mongodb://127.0.0.1/weboff?retryWrites=true&w=majority"
mongo = PyMongo(app)
#CORS(app)
 

#base="https://blogmarksmart.herokuapp.com"
#base="http://127.0.0.1:5000"


from app import routes
