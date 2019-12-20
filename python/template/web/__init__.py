from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from config import Config

application = Flask(__name__)

application.config.from_object(Config)
CORS(application)
jwt = JWTManager(application)

db = SQLAlchemy(application)
migrate = Migrate(application, db)

import app
from .views import index
import test