from flask import Blueprint                                # Importing the Bllueprint class from flask  

auth = Blueprint('auth', __name__, url_prefix="/auth")     # Creating the auth blueprint into a varaibale called auth

@auth.route("/register", methods=["POST"])                 # Register route
def auth_register():
    return "working"