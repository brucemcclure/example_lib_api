from dotenv import load_dotenv # This is the package used to set env varibles
load_dotenv()                  # Load the env variables

from flask import Flask       # Importing the flask class
app = Flask(__name__)         # Creating an app instnace from the flask class

from database import init_db
db = init_db(app) # Db connection

from controllers import registerable_controllers # Importing the various controllers
for controller in registerable_controllers: # Looping over the registerable_controllers and registering them
    app.register_blueprint(controller)


