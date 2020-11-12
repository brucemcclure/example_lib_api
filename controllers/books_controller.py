from models.Book import Book                                  # This is the module that will communicate with the book table
from models.User import User                                  # This is the module that will communicate with the user table
from main import db                                           # Db connection
from flask import Blueprint, request, jsonify, abort          # We need to be able to create a blueprint and retrieve and send back data
from schemas.BookSchema import books_schema, book_schema      # Importing the serialization module
from flask_jwt_extended import jwt_required, get_jwt_identity # This function will check if we have a JWT sent along with our request or not
books = Blueprint("books", __name__, url_prefix="/books")     # Creating the blueprint and specifying the url_prefix


# These are examples of raw sql crud. They will be replaced with a ORM soon

#Return all books
@books.route("/", methods=["GET"])
def book_index():
    books = Book.query.all()                   # Using the Book model to fetch all the books with the query method
    return jsonify(books_schema.dump(books))   # Return the data in the form of JSON
    

#Create a new book
@books.route("/", methods=["POST"])                 # Define the route and method
@jwt_required
def book_create():                                  # Define the create function

    book_fieds = book_schema.load(request.json)     # Deserializing the json into something that can be used
    user_id = get_jwt_identity()                    # Get identity returns the userid from the JWT
    user = User.query.get(user_id)                  # Return the user from querying the DB with the DB
    if not user:                                    # If no user then return the id
        return abort(401, description="Invalid user")

    new_book = Book()                           # Creating a new instance of book
    new_book.title = book_fieds["title"]        # Update the title

    user.books.append(new_book)                 # Add this book to the the user who created it
    db.session.commit()                         # Commit the transaction
    return jsonify(book_schema.dump(new_book))  # Return the json format of the book



# Return a single book
@books.route("/<int:id>", methods=["GET"])      # Define the route and method
def book_show(id):                              # Define the show function, , takes the id as an argument
    book = Book.query.get(id)                   # Using the Book model to fetch one book with a specific id using the query method
    return jsonify(book_schema.dump(book))      # Return the book in the form of JSON


# Update a book
@books.route("/<int:id>", methods=["PUT", "PATCH"])     # Define the route and method
@jwt_required
def book_update(id):                                    # Define the update function, takes the id as an argument
    books = Book.query.filter_by(id=id)                 # Using the Book model to fetch one book with a specific id using the query method
    book_fields = book_schema.load(request.json)        # Deserializing the json into something that can be used
    books.update(book_fields)                           # Update books with the new data
    db.session.commit()                                 # Commit the transaction to the DB
    return jsonify(book_schema.dump(books[0]))          # Return the data

# Delete a book
@books.route("/<int:id>", methods=["DELETE"])      # Define the route and method
@jwt_required
def book_delete(id):                               # Define the update function, takes the id as an argument
    book = Book.query.get(id)                      # Get a reference to the specific book using the Book model and the query method
    db.session.delete(book)                        # Delete the book
    db.session.commit()                            # Commit the transaction to the database
    return jsonify(book_schema.dump(book))         # Return the data in the form of json