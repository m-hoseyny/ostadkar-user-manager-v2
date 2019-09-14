from flask import Flask
from app import db
from .config import app_config
import environ
import os
from .routes import register_routes
from flask_login import LoginManager

# from app.UserManager.UserModel import User


ENV_NAME = os.getenv('FLASK_ENV')

env = environ.Env()
environ.Env.read_env('.env')
flask_configs = app_config[ENV_NAME]

app = Flask(__name__)

app.config.from_object(flask_configs)
db.init_app(app)
app.app_context().push()

register_routes(app)

login_manager = LoginManager()
login_manager.init_app(app)

# Create Tables
db.create_all()


@app.route('/', methods=['GET'])
def index():
    return 'This is user manager API'

