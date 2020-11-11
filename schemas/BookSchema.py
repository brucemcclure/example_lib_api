from main import ma                          # Importing the instnace of ma, which has app registered with it. 
from models.Book import Book                 # Importing the model that handles the book database.
from marshmallow.validate import Length      # This is the validator module in marshmallow



# Because we are using the auto schema marshmello will auto update the schema when we change the book model 
class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Book
    title = ma.String(required=True, validate=Length(min=1))        # This is declaring a required data type on the title column

book_schema = BookSchema()                  # How you serilaize and deserialize one object.
books_schema = BookSchema(many = True)      # How you serilaize and deserialize many objects.