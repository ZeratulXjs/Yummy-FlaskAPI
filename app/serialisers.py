from flask_restplus import fields
from app.yum_api import api

user_acc = api.model('User details', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a user'),
    'name': fields.String(required=True, description='User name'),
    'email': fields.String(required=True, description='User email address'),
    'password': fields.String(required=True, description='Encrypted user password')    
})

users_list = api.model('Page of Yummy Users', {
  'items': fields.List(fields.Nested(user_acc))
})


