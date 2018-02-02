import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

# Local imports
from run import create_app
from app.models import db, Users, Recipes


# Set variables
app = create_app(config_name=os.getenv('APP_SETTINGS'))

'''
For any changes in the models, migrations will be managed by
Flask-Migrate and external scripts will be run through Flask-Script

'''

manager = Manager(app)
migrate = Migrate(app,db)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
	manager.run()
