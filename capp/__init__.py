from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

application = Flask(__name__)

### Code GitHub
application.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
# DBVAR=os.environ['DATABASE_URL']
DBVAR="postgresql://blhpjleisftrnu:51669098ea30d9afe03f32061ab3ea57fa0216202821f103a571832335d74541@ec2-34-241-82-91.eu-west-1.compute.amazonaws.com:5432/ddrueu2bqi58l"
# DBVAR="postgresql://username:password@host:port/database"
application.config['SQLALCHEMY_DATABASE_URI'] = DBVAR 
application.config['SQLALCHEMY_BINDS'] ={'transport': DBVAR}


db = SQLAlchemy(application)
bcrypt = Bcrypt(application)
login_manager= LoginManager(application)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

from capp.home.routes import home
from capp.methodology.routes import methodology
from capp.carbon_app.routes import carbon_app
from capp.users.routes import users

application.register_blueprint(home)
application.register_blueprint(methodology)
application.register_blueprint(carbon_app)
application.register_blueprint(users)

