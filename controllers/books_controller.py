from models.Book import Book                              # This is the module that will communicate with the book table
from main import db                                       # Db connection
from flask import Blueprint, request, jsonify             # We need to be able to create a blueprint and retrieve and send back data
from schemas.BookSchema import books_schema, book_schema  # Importing the serialization module
books = Blueprint("books", __name__, url_prefix="/books") # Creating the blueprint and specifying the url_prefix


# These are examples of raw sql crud. They will be replaced with a ORM soon

#Return all books
@books.route("/", methods=["GET"])
def book_index():
    books = Book.query.all()                   # Using the Book model to fetch all the books with the query method
    return jsonify(books_schema.dump(books))   # Return the data in the form of JSON
    

#Create a new book
@books.route("/", methods=["POST"])
def book_create():
    book_fieds = book_schema.load(request.json) # Deserializing the json into something that can be used
    new_book = Book()                           # Creating a new instance of book
    new_book.title = book_fieds["title"]        # Update the title
    db.session.add(new_book)                    # Add the book to the session
    db.session.commit()                         # Commit the transaction
    return jsonify(book_schema.dump(new_book))  # Return the json format of the book



# @books.route("/<int:id>", methods=["GET"])
# def book_show(id):
#     #Return a single book
#     sql = "SELECT * FROM books WHERE id = %s;"
#     cursor.execute(sql, (id,))
#     book = cursor.fetchone()
#     return jsonify(book)

# @books.route("/<int:id>", methods=["PUT", "PATCH"])
# def book_update(id):
#     #Update a book
#     sql = "UPDATE books SET title = %s WHERE id = %s;"
#     cursor.execute(sql, (request.json["title"], id))
#     connection.commit()

#     sql = "SELECT * FROM books WHERE id = %s"
#     cursor.execute(sql, (id,))
#     book = cursor.fetchone()
#     return jsonify(book)

# @books.route("/<int:id>", methods=["DELETE"])
# def book_delete(id):
#     sql = "SELECT * FROM books WHERE id = %s;"
#     cursor.execute(sql, (id,))
#     book = cursor.fetchone()
    
#     if book:
#         sql = "DELETE FROM books WHERE id = %s;"
#         cursor.execute(sql, (id,))
#         connection.commit()

#     return jsonify(book)