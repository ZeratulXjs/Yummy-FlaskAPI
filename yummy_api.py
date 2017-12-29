from os import urandom
import uuid
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api
from models import db
from endpoint_classes import UserList, UserUpdate

app = Flask(__name__)

POSTGRES = {
  'user' : 'postgres', 
  'pw' : 'postgres',  
  'host' : 'localhost',
  'port' : '5432',
  'db' : 'YummyUsers',
}

app.config["SECRET_KEY"] = urandom(32)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s" % POSTGRES
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
ma = Marshmallow(app)
api = Api(app)


@app.route('/', methods=['GET'])
def index():
  return jsonify({"message":"Welcome to the Yummy-FlaskAPI! To see what we have, create an account!"})

#Define API endpoints -- Map classes to API endpoints
api.add_resource(UserList, '/user.json')
api.add_resource(UserUpdate, '/user/<int:id>.json')

if __name__ == "__main__":
  app.run(debug=True)
