from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

app = Flask(__name__)


app.config["SECRET_KEY"] = "0555510986"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqlalshemy.db"



db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = "login"

from Qudurat import routes
