from database import cursor, connection
from flask import Blueprint, request, jsonify
authors = Blueprint("authors", __name__, url_prefix="/authors")


@authors.route("/", methods=["GET"])
def author_index():
    

    return "all authors"