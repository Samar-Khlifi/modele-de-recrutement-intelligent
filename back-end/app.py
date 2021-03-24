from flask import Flask
import pymongo
from flask_restful import Api
from database.db import initialize_db
from flask_jwt_extended import JWTManager#pour sécuriser token
#cors:




app=Flask(__name__)
jwt = JWTManager(app)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER


app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost:27017/samar'
}
app.config['SECRET_KEY'] = 'itgate'
myclient=pymongo.MongoClient("mongodb://127.0.0.1:27017/")
mydb=myclient['samar']

from Resources.routes import initialize_routes

api = Api(app)
initialize_db(app)
initialize_routes(api)

