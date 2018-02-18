from passlib.hash import sha256_crypt

# local imports
from app.models import db, Users, Recipes

'''
Create items
'''
def create_user(data):
  name = data.get('name')
  email = data.get('email')
  password = sha256_crypt.encrypt(str(data.get('password')))
  user = Users(name, email, password)
  Users.add(user)
    
def create_recipe(data):
  title = data.get('title')
  text = data.get('text')
  recipe = Recipes(title, text)
  Recipes.add(recipe)

'''
Read items
'''

def read_user_list(data):
  pass

def read_user(data):
  pass

def read_recipe_list(data):
  pass
  
def read_recipe(data):
  pass

'''
Update items
'''

def update_recipe(recipe_id, data):
  recipe = Recipes.query.filter(Recipes.id == recipe_id).one()
  recipe.title = data.get('title')
  recipe.text = data.get('text')
  Recipes.update(recipe)

'''
Delete items
'''

def delete_user(data):
  pass

def delete_recipe(recipe_id):
  recipe = Recipes.query.filter(Recipes.id == recipe_id).one()
  Recipes.delete(recipe)
