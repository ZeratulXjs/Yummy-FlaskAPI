from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class CRUD(): 
  ''' 
  Base model containing the CRUD functionality that 
  connects to the database via SQLAlchemy sessions

  '''

  def add(self, Resource):
    db.session.add(Resource)
    return db.session.commit()

  def update(self):
    return db.session.commit()

  def delete(self, Resource):
    db.session.delete(Resource)
    return db.session.commit()

class Users(db.Model, CRUD):
  ''' 
  Model for users which will inherit Flask-SQLAlchemy Model
  class and the CRUD class defined above
    
  '''

  __tablename__ = 'YummyUsers'

  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(50), nullable = False)
  email = db.Column(db.String(50), unique = True, nullable = False)
  password = db.Column(db.String(400))
  

  def __init__(self, name, email, password):
    self.name = name
    self.email = email
    self.password = password

  def __repr__(self):
    return '<User %r>' % self.public_id

class Recipes(db.Model, CRUD):
  ''' 
  Model for recipes 
  
  '''

  __tablename__ = 'YummyRecipes'

  id = db.Column(db.Integer, primary_key = True)
  title = db.Column(db.String(50), nullable = False)
  text = db.Column(db.String(250), nullable = False)
  date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
  if date_created is None:
    date_created = DateTime.utcnow()
  date_modified = db.Column(
    db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp()
  )
  if date_modified is None:
    date_modified = date_created
  
  author = db.relationship('Users', backref=db.backref('recipes', lazy='dynamic'))
  
  def __init__(self, title, text, date_created=None, date_modified=None):
    self.title = title
    self.text = text
    self.date_created = date_created
    self.date_modified = date_modified
    
  def __repr__(self):
    return '<Recipe %r>' % self.title
