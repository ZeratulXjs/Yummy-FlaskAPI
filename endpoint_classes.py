from passlib.hash import sha256_crypt
from models import Users, Recipes, UserSchema, RecipeSchema, db
from flask_restful import Api, Resource

#Declare an instance of the UserSchema and Flask-Restful Api class
schema = UserSchema()
api = Api()


#The following class will be used for GET and POST requests to /users

class UserList(Resource):
  #Function for a GET request
  def get(self):
    #Query the database and return all users
    users_query = Users.query.all()
    #Serialize the query results in the JSON API format
    results = schema.dump(users_query, many=True).database
    return results

  #Function for the POST request
  def post(self):
    raw_dict = request.get_json(force=True)
    user_dict = raw_dict['data']['attributes']
    hashed_password = sha256_crypt.encrypt(str(user_dict['password']))
    password_dict = {'password':hashed_password}
    try:
      #Validate the data or raise a Validation error if incorrect 
      schema.Validate(user_dict)
      #Create a User object with the API data recieved 
      user = Users(user_dict['name'], user_dict['email'], password_dict['password'])
      #Commit data
      user.add(user)
      query = Users.query.get(user_id)
      results = schema.dump(query).data
      return results, 201

    except ValidationError as err:
      resp = jsonify({"error" : err.messages})
      resp.status_code = 403
      return resp

    except SQLAlchemyError as e:
      db.session.rollback()
      resp = jsonify({"error" : str(e)})
      resp.status_code = 403
      return resp

#The following class is used when a GET, PUT, DELETE HTTP request is sent to /user/{user_id}

class UserUpdate(Resource):
  def get(self, id):
    users_query = Users.query.get_or_404(id)
    result = schema.dump(users_query).data
    return result

  def put(self, id):
    user = Users.query.get_or_404(id)
    raw_dict = request.get_json(force = True)
    user_dict = raw_dict['data']['attributes']
    try:
      for key, value in user_dict.items():
        schema.Validate({key:value})
        setattr(user, key, value)
        user.update()
      return self.get(id)
    except ValidationError as err:
      resp = jsonify({"error" : err.messages})
      resp.status_code = 401
      return resp

  def delete(self, id):
    user = Users.query.get_or_404(id)
    try:
      delete = user.delete(user)
      response = make_response()
      response.status_code = 204
      return response
    except SQLAlchemyError as e:
      db.session.rollback()
      resp = jsonify({"error" : str(e)})
      resp.status_code = 401
      return resp
