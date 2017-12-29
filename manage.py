from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from yummy_api import app,db

'''
To manage any changes in the models, migrations will be managed by
Flask-Migrate and external scripts will be run through Flask-Script

'''

manager = Manager(app)
migrate = Migrate(app,db)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
	manager.run()
