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

class Users(db.Model, CRUD):
  ''' Model for users which will inherit Flask-SQLAlchemy Model
      class and the CRUD class defined above'''

  __tablename__ = 'YummyUsers'

  id = db.Column(db.Integer, primary_key = True)
  public_id = db.Column(db.String(50), nullable = False)
  name = db.Column(db.String(50), nullable = False)
  email = db.Column(db.String(50), unique = True, nullable = False)
  password = db.Column(db.String(300))

  def __init__(self, public_id, name, email, password):
    self.public_id
    self.name = name
    self.email = email
    self.password = password

class UserSchema(Schema):
  not_blank = validate.Length(min=1, error='Field cannot be blank')
  id = fields.Integer(dump_only = True)
  name = fields.String(validate = not_blank)
  email = fields.Email(validate = not_blank)
  password = fields.String(validate = not_blank)

  #self links
  def get_top_level_links(self, data, many):
    if many:
      self_link = "/users/"
    else:
      self_link = "/users/{}".format(data['id'])
    return{'self': self_link}
    
  class Meta:
    type_ = 'users'


class Recipes(db.Model, CRUD):
  ''' Model for recipes '''

  __tablename__ = 'YummyRecipes'

  id = db.Column(db.Integer, primary_key = True)
  title = db.Column(db.String(50), nullable = False)
  text = db.Column(db.String(250), nullable = False)
  
  def __init__(self, title, text):
    self.title = title
    self.text = text

class RecipeSchema(Schema):
  not_blank = validate.Length(min=1, error='Field cannot be blank')
  id = fields.Integer(dump_only = True)
  title = fields.String(validate = not_blank)
  text = fields.String(validate = not_blank)

  #self links
  def get_top_level_links(self, data, many):
    if many:
      self_link = "/recipes/"
    else:
      self_link = "/recipes/{}".format(data['id'])
    return{'self': self_link}
    
  class Meta:
    type_ = 'recipes'
