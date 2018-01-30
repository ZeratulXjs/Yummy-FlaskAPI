# System imports
from flask import request
from flask_restplus import Resource

# Local imports
from app.yum_api import api
from app.models import Users, Recipes
from app.database_logic import create_user, create_recipe, update_recipe, delete_recipe
from app.serialisers import user_acc, users_list
from app.parsers import pagination_arguments

#The following namespace will define functions related to Yummy Users

ns_users = api.namespace('yummy/users', description='Operations related to YummyAPI Users')

@ns_users.route('/')
class AllUsers(Resource):
  
  @api.marshal_with(users_list)
  def get(self):
    '''
    Returns list of users in the database
    '''
    users_query = Users.query
    return users_query
