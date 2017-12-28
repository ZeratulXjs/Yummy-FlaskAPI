from flask_sqlalchemy import SQLAlchemy
from marshmallow import validate
from marshmallow_jsonapi import Schema, fields

db = SQLAlchemy()

class CRUD():
  ''' Base model containing the CRUD functionality that 
      connects to the database via SQLAlchemy sessions'''

  def add(self, resource):
    db.session.add(resource)
    return db.session.commit()

  def update(self):
    return db.session.commit()

  def delete(self, resource):
    db.session.delete(resource)
    return db.session.commit()

class Users(db.model, CRUD):
  ''' Model for users '''

  __tablename__ = 'YummyUsers'

  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(50), nullable = False)
  email = db.Column(db.String(50), unique = True, nullable = False)

  def __init__(self, name, email, password):
    self.name = name
    self.email = email
    self.password = password

  def __repr__(self):
    return '<id {}>'.format(self.id)
