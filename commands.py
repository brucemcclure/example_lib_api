from main import db                         # DB connection
from flask import Blueprint                 # Using a flask Blueprint because passing the app around is bad practice

db_commands = Blueprint("db-custom", __name__)     # Creating the blueprint


# @db_commands.cli.command("create")          # The 'create' command
# def create_db():                            # Declaration of the function
#     db.create_all()
#     print("Tables created!")


@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()                                               # This command drops tables connected to models
    db.engine.execute("DROP TABLE IF EXISTS alembic_version;")  # Drop the alembic_version table if it exists
    print("Tables deleted")


@db_commands.cli.command("seed")           # The seed command
def seed_db():
    from models.Book import Book           # Import the book model
    from models.User import User           # User model
    from main import bcrypt                # Hashing module
    from faker import Faker                # Import the faker module
    import random

    faker = Faker()                        # Create an instance of faker
    users = []                             # Initializing an empty list

    # Creating 5 users and appending them to the users list
    for i in range(5):
        user = User()
        user.email = f"test{i}@test.com"
        user.password = bcrypt.generate_password_hash("123456").decode("utf-8")
        db.session.add(user)
        users.append(user)

    db.session.commit()

    for i in range(20):                        # 20
        book = Book()                          # New instance of book
        book.title = faker.catch_phrase()      # Add a title
        book.user_id = random.choice(users).id  # Choosing a random user to assign the book to
        db.session.add(book)                   # add the book to the db session

    db.session.commit()                        # Commit all the books to the db
    print("Tables seeded")
