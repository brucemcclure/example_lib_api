from dotenv import load_dotenv                              # This is the package used to set env varibles
load_dotenv()                                               # Load the env variables

from marshmallow.exceptions import ValidationError

from flask import Flask, jsonify                            # Importing the flask class
app = Flask(__name__)                                       # Creating an app instnace from the flask class
app.config.from_object("default_settings.app_config")       # Loads our configuration from defatult_settings.py

from database import init_db
db = init_db(app)                                           # Db connection

# Serialization and Deserialization
from flask_marshmallow import Marshmallow                   # Importing the package 
ma = Marshmallow(app)                                       # Making a 'ma' object out of the Marshmellow class with app as the argument. 

from commands import db_commands                            # Import the db commands
app.register_blueprint(db_commands)                         # Register the commands with app

from controllers import registerable_controllers            # Importing the various controllers
for controller in registerable_controllers:                 # Looping over the registerable_controllers and registering them
    app.register_blueprint(controller)


@app.errorhandler(ValidationError)                          # Decorator for the ValidationError
def handle_bad_request(error):                              # The handle bad request function inherits from the python error object
    return (jsonify(error.messages), 400)                   # Return the  error message in jason with a status of 400