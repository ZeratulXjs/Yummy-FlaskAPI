from os import urandom

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

SECRET_KEY = urandom(32)
SQLALCHEMY_DATABASE_URI = "postgresql://Banana:Banana1@localhost/yummy_db"