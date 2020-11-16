# When you import a directory but you havent given a specific file name then it will import __init__.py by default

from controllers.books_controller import books              # Importing the books blueprint
from controllers.auth_controller import auth                # Importing the auth blueprint
from controllers.book_images_controller import books_images  # Importing the book images blueprint

registerable_controllers = [
    books,
    auth,
    books_images
]
