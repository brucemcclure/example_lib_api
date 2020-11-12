from models.User import User                               # User model
from schemas.UserSchema import user_schema                 # User Schema
from main import db                                        # Importing the db
from flask import Blueprint, request, jsonify, abort       # Importing the Blueprint class from flask  

auth = Blueprint('auth', __name__, url_prefix="/auth")     # Creating the auth blueprint into a varaibale called auth

@auth.route("/register", methods=["POST"])                 # Register route
def auth_register():
    user_fields = user_schema.load(request.json)                       # Getting the fields form the user schema in json format
    user = User.query.filter_by(email=user_fields["email"]).first()    # Checking if the email sent through has already been registered

    if user:                                                           
         return abort(400, description="Email already registered")     # If the email is already in use then return this error

    user = User()                                                      # Create a new user object
    user.email = user_fields["email"]                                  # Assign the email to the user
    user.password = user_fields["password"]                            # Assign the password to the user

    db.session.add(user)                                               # Add the commited user to the session   
    db.session.commit()                                                # Commit the session to the database

    return jsonify(user_schema.dump(user))                             # Return the user in JSON format