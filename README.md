# Yummy-FlaskAPI

This an API written in python using the Flask framework. It uses PostgreSQL for data persistence.
Users can create accounts, login and submit recipes. They can also view submitted recipes in the database.

Development was done using Ubuntu, so the instructions in this README are specific to that OS.

The API uses the following core dependencies/modules;

```linux
Python 3.4
Flask
Flask-SQLAlchemy
Flask-Marshmallow
Alembic
PostgreSQL

```

The complete list of depencies and their versions can be found in the `requirements.txt` file.

## Running the API

1. Clone this repo to a local directory;

`clone https://github.com/ZeratulXjs/Yummy-FlaskAPI.git`

2. Install PostgreSQL. Add a new system user and create the Postgres database that the API will use;
    You can change the password to whatever you like, then change it in the yummy_api app too.

```linux
sudo apt-get install postgresql postgresql-contrib

sudo -i -u postgres psql

CREATE USER postgres WITH PASSWORD 'postgres';

CREATE DATABASE YummyAPI OWNER postgres;

\q
```

3. Activate the virtual environment and install dependencies/modules;

```linux
  virtualenv -p /usr/bin/python-3.4 venv-3.4

  source venv-3.4/bin/activate

  pip install requirements.txt
```

4. Activate migration of the users and recipes tables to the database you created;

```linux
python manage.py db init

python manage.py db migrate

python manage.py db upgrade
```

5. Once that database and tables have been created, run tests on the API;

`pytest test_yummy_api.py`

Passing tests are satisfying to watch, yeah?

6. Test the API using Postman;
