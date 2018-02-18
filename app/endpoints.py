# System imports
from flask import request
from flask_restplus import Resource

# Local imports
from app.yum_api import api
from app.models import Users, Recipes
from app.database_logic import create_user, create_recipe, read_user_list, read_recipe_list, read_user, read_recipe, update_recipe, delete_user, delete_recipe
from app.serialisers import user_acc, users_list, recipe_entry, recipes_list, recipe_detail


#The following namespace will define functions related to Yummy Users

ns_users = api.namespace('users', description='Operations related to YummyAPI Users')

@ns_users.route('/')
class AllUsers(Resource):
  
  @api.marshal_with(users_list)
  def get(self):
    '''
    Returns list of users in the database
    '''
    users_query = Users.query
    return users_query

  @api.expect(user_acc)
  def post(self):
    '''
    Creates a new user
    '''
    create_user(request.json)
    return {'user': 'New user registered!'}, 201

ns_recipes = api.namespace('recipes', description='Operations related to YummyAPI Recipes')    

@ns_recipes.route('/')
class AllRecipes(Resource):

    @api.marshal_with(recipes_list)
    def get(self):
      '''
      Returns list of recipes in the database
      '''
      recipes_query = Recipes.query
      return recipes_query 
