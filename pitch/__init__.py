#Initialize our Pitch App here
#Initialize the Flask App
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)

app.config['SECRET_KEY'] = '052ffd3a3b34217849c58c98ca017db4'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'#USE POSTGRE LATER ON!!
#Create db instance
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

#Import here to prevent circular imports
from pitch import routes