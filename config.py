from os import urandom

POSTGRES = {
  'user' : 'postgres', 
  'pw' : 'postgres',  
  'host' : 'localhost',
  'port' : '5432',
  'db' : 'YummyUsers',
}

app.config["SECRET_KEY"] = urandom(32)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s" % POSTGRES
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
