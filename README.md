# Yummy-FlaskAPI

An API for the YummyRecipes project 

The API uses the following core dependencies/modules;

```linux
Python 3.4
Flask
Flask-SQLAlchemy
Flask-Marshmallow
Flask-Migrate
PostgreSQL

```

The complete list of depencies and their versions can be found in the `requirements.txt` file.

## Running the API

1. Clone this repo to a local directory;

`clone https://github.com/ZeratulXjs/Yummy-FlaskAPI.git`

2. Activate the virtual environment and install dependencies/modules

```linux
  virtualenv -p /usr/bin/python-3.4 venv-3.4

  source venv-3.4/bin/activate

  pip install requirements.txt
```

3. Create a new system user and create the Postgres database the API will use assigned to that user

```linux
sudo adduser postgres_user

sudo -i -u postgres psql

CREATE USER postgres_user WITH PASSWORD 'password';

CREATE DATABASE YummyUsers OWNER postgres_user;

\q
```

4. Activate migration of the users and recipes tables to the database you created

```linux
python manage.py db init

python manage.py db migrate

python manage.py db upgrade
```

5. Once that database and tables have been created, run tests on the app

`pytest test_yummy_api.py`

6. 
