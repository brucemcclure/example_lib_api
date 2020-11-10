from database import cursor, connection # Importing the dd config because we need acess to it in this file
from flask import Blueprint, request, jsonify # We need to be able to create a blueprint and retrieve and send back data
authors = Blueprint("authors", __name__, url_prefix="/authors") # Creating the blueprint and specifying the url_prefix

# This is a dummy endpoint
@authors.route("/", methods=["GET"])
def author_index():
    return "all authors"