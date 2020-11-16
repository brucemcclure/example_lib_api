# 99% of the time you want a model for each table in the db.
from main import db  # db connection
from models.BookImage import BookImage                                              # This is needed to auto build the relationship


class Book(db.Model):
    __tablename__ = "books"  # declaring the name of the table in the db
    # The name of the attribute maps to the name of the column on the table

    id = db.Column(db.Integer, primary_key=True)                                    #
    title = db.Column(db.String())                                                  #
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)      #
    book_image = db.relationship("BookImage", backref="book", uselist=False)        #

    def __repr__(self):  # Representitive state
        return f"<Book {self.title}>"  # When its printed you can now see the title instead of the id
