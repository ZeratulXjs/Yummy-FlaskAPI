# system imports
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# local imports
from instance import config
from instance.config import app_config
from app.yum_api import api
from app.models import db
import app.endpoints

config_name = os.getenv('APP_SETTINGS') # config_name = "development"

def create_app(config_name):
  app = Flask(__name__)


  app.config.from_object(app_config[config_name])
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
  api.init_app(app)  
  db.init_app(app)
  return app
 
  
if __name__ == "__main__":
  create_app(config_name).run(debug=True)  
