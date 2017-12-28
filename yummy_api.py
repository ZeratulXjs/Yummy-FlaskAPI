from os import urandom
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_heroku import Heroku
from models import db

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
heroku = Heroku(app)

@app.route('/', methods=['GET'])
def index():
  return jsonify({'message':"Welcome to the Yummy-FlaskAPI! To see what we have, create an account!"})
 


if __name__ == "__main__":
  app.run(debug=True)
