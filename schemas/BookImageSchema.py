from main import ma                          # Importing the instnace of ma, which has app registered with it.
from models.BookImage import BookImage       # Importing the model that handles the book database.
from marshmallow.validate import Length      # This is the validator module in marshmallow


class BookImageSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = BookImage

    filename = ma.String(required=True, validate=Length(min=1))


book_image_schema = BookImageSchema()
