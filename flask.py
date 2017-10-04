from flask import Flask, render_template, jsonify, abort, request
from flask.ext.restless import APIManager 
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

class Developer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Colum(db.String(20))
    hireDate = db.Colum(db.Date)
    focus = db.Colum(db.String(50))


def __init__(self, name, hireDate, focus)
    self.name = name
    self.hireDate = datetime.datetime.strptime(hireDate, %d%m%y).date()
    self.focus = focus

db.createAll()

@app.route('/dev/', methods=['GET'])
def index():
    return jsonify({ 'Developers': Developer.querry.get(id)})