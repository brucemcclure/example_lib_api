from main import db                         # DB connection
from flask import Blueprint                 # Using a flask Blueprint because passing the app around is bad practice

db_commands = Blueprint("db", __name__)     # Creating the blueprint

@db_commands.cli.command("create")          # The 'create' command 
def create_db():                            # Declaration of the function
    db.create_all()                         
    print("Tables created!")

@db_commands.cli.command("drop")            # The 'create' command 
def drop_db():                              # Declaration of the function
    db.drop_all()
    print("Tables deleted")


@db_commands.cli.command("seed")           # The seed command
def seed_db():
    from models.Book import Book           # Import the book model
    from faker import Faker                # Import the faker module 
    faker = Faker()                        # Create an instance of faker

    for i in range(20):                    # 20
        book = Book()                      # New instance of book
        book.title = faker.catch_phrase()  # Add a title
        db.session.add(book)               # add the book to the db session
    
    db.session.commit()                    # Commit all the books to the db
    print("Tables seeded")