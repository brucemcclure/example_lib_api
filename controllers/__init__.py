# When you import a directory but you havent given a specific file name then it will import __init__.py by default

from controllers.books_controller import books # Importing the books blueprint
from controllers.auth_controller import auth   # Importing the auth blueprint

registerable_controllers = [
    books,
    auth
]


