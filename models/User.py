from main import db                                                 # Importing the db from main 

class User(db.Model):                                               # This is the the User class that inherits from db.Model
    __tablename__ = "users"                                         # This explicitally names the table 'users'

    id = db.Column(db.Integer, primary_key=True)                    # The id is the primary key
    email = db.Column(db.String(), nullable=False, unique=True)     # The emails is a string and mustbe unique
    password = db.Column(db.String(), nullable=False)               # The password is a string and cannot be null
    books = db.relationship("Book", backref="user", lazy="dynamic") # Relating back to the book table

    def __repr__(self):                                             # 
        return f"<User {self.email}>"                               #