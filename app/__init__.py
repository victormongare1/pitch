from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_simplemde import SimpleMDE

bootstrap = Bootstrap()
simple=SimpleMDE()
db=SQLAlchemy()
def create_app(config_name):
  # Initializing application
  app = Flask(__name__)
  # Setting up configuration
  app.config.from_object(config_options[config_name])
  # Initializing Flask Extensions
  bootstrap.init_app (app)
  simple.init_app(app)
  db.init_app(app)
  # Registering the blueprint
  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)
  return app