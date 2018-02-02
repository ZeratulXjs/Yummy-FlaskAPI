from os import urandom
from flask_sqlalchemy import SQLAlchemy

POSTGRES = {
  'user' : 'postgres', 
  'pw' : 'postgres',  
  'host' : 'localhost',
  'port' : '5432',
  'db' : 'yummyapi',
}

class Config(object):
  # Parent configuration class 
  DEBUG = False
  CSRF_ENABLED = True 
  SECRET_KEY = urandom(32)
  SQLALCHEMY_DATABASE_URI = "postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s" % POSTGRES

class DevelopmentConfig(Config):
  # Development configurations 
  DEBUG = True

class TestingConfig(Config):
  # Configurations for Testing, with a separate testing database 
  TESTING = True
  SQLALCHEMY_DATABASE_URI = "postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/test_db" % POSTGRES
  DEBUG = True

class StagingConfig(Config):
  # Configurations for Staging
  DEBUG = True

class ProductionConfig(Config):
  # Configurations for Production
  TESTING = False

app_config = {
  'development' : DevelopmentConfig,
  'testing' : TestingConfig,
  'staging' : StagingConfig,
  'production' : ProductionConfig
}
