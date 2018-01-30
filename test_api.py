import unittest
import run
import models
import manage


#Test different classes for valid input acceptance and processing
class UserdbTestCase(unittest.TestCase):
    def setUp(self):
        self.userdb = Users()
        