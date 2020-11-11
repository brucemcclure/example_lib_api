from dotenv import load_dotenv                              # This is the package used to set env varibles
load_dotenv()                                               # Load the env variables

from flask import Flask                                     # Importing the flask class
app = Flask(__name__)                                       # Creating an app instnace from the flask class
app.config.from_object("default_settings.app_config")                  # Loads our configuration from defatult_settings.py


from database import init_db
db = init_db(app)                                           # Db connection

# Serialization and Deserialization
from flask_marshmallow import Marshmallow # Importing the package 
ma = Marshmallow(app)                     # Making a 'ma' object out of the Marshmellow class with app as the argument. 

from controllers import registerable_controllers # Importing the various controllers
for controller in registerable_controllers: # Looping over the registerable_controllers and registering them
    app.register_blueprint(controller)


