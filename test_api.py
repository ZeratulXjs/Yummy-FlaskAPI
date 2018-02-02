# System imports
import unittest

# Local imports
from instance import config
from instance.config import app_config
from app.yum_api import api
from app.models import db, Users, Recipes
from app.database_logic import create_user, create_recipe, update_recipe, delete_recipe
from app.serialisers import user_acc, users_list
from app.parsers import pagination_arguments
from app.endpoints


#Test different classes for valid input acceptance and processing
class UserdbTestCase(unittest.TestCase):
    def setUp(self):
        self.userdb = Users()
        
