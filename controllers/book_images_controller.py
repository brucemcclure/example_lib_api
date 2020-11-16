from flask import Blueprint, request, jsonify, abort, current_app, Response
from flask_jwt_extended import jwt_required
from services.auth_service import verify_user
from models.BookImage import BookImage
from models.Book import Book
from schemas.BookImageSchema import book_image_schema
import boto3                                            # Automatically imports aws variables from .env
from main import db                                     # Needs access to the db
from pathlib import Path

book_images = Blueprint("book_images", __name__, url_prefix="/books/<int:book_id>/image")  # The book id is the book the image is assiciated with

# NB if flaask receives an image it puts it in a dictionary called request.files


@book_images.route("/", methods=["POST"])
@jwt_required
@verify_user
def book_image_create(book_id, user=None):
    book = Book.query.filter_by(id=book_id, user_id=user.id).first()            # Check if the book exisits and the user owns that book

    if not book:                                                                # Check if the book exists
        return abort(401, description="Invalid book")

    if "image" not in request.files:                                            # Check if there is an image on the post request
        return abort(400, description="No Image")

    image = request.files["image"]                                              # Assign the image to the variable

    if Path(image.filename).suffix not in [".png", ".jpeg", ".jpg", ".gif"]:    # Check if the correct file suffix is on the file
        return abort(400, description="Invalid file type")

    filename = f"{book_id}{Path(image.filename).suffix}"                        # Create the file name
    bucket = boto3.resource("s3").Bucket(current_app.config["AWS_S3_BUCKET"])   # Connect to the bucket
    key = f"book_images/{filename}"                                             # File path

    bucket.upload_fileobj(image, key)                                           # Uplaod the image

    if not book.book_image:                                                     # If there is no book image then create one and commit to the db
        new_image = BookImage()
        new_image.filename = filename
        book.book_image = new_image
        db.session.commit()

    return ("", 201)


# Because the bucket is not accessable to the public:
# We will download the image and pipe it directly inot the api respose.

@book_images.route("/<int:id>", methods=["GET"])
def book_image_show(book_id, id):
    book_image = BookImage.query.filter_by(id=id).first()                       # Grab the book  from the database

    if not book_image:                                                          # Make usre the book exists
        return abort(401, description="Invalid book")

    bucket = boto3.resource("s3").Bucket(current_app.config["AWS_S3_BUCKET"])  # Assign the S3
    filename = book_image.filename
    file_obj = bucket.Object(f"book_images/{filename}").get()                   # This gets the actual file form S3. This is a Stream

    print(file_obj)                                                             # Printing the file

    return Response(
        file_obj["Body"].read(),                                                # This information is piped in from the stream
        mimetype="image/*",                                                     # This is the media type for the request or mimetype
        headers={"Content-Disposition": "attachment;filename=image"}            # Telling the F-End that there is an attachment and a filename called image
    )


@book_images.route("/<int:id>", methods=["DELETE"])
@jwt_required
@verify_user
def book_image_delete(book_id, id, user=None):
    book = Book.query.filter_by(id=book_id, user_id=user.id).first()

    if not book:
        return abort(401, description="Invalid book")
    if book.book_image:
        bucket = boto3.resource("s3").Bucket(current_app.config["AWS_S3_BUCKET"])
        filename = book.book_image.filename

        bucket.Object(f"book_images/{filename}").delete()

        db.session.delete(book.book_image)
        db.session.commit()

    return jsonify("", 204)
