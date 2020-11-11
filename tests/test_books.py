import unittest                                     # This is the inbuilt python testing module
from main import create_app


class TestBooks(unittest.TestCase):                 # This is the Parent class that will test our books module. 
    def test_book_index(self):
        app = create_app()                          # This is an instance of app
        client = app.test_client()                  # This helps us make http requests to the app while we are testing
        response = client.get("/books/")            # make a get request to the "/books/" url, save it to a response object

        data = response.get_json()
        self.assertEqual(response.status_code, 200) # Checking if the response code is 200
        self.assertIsInstance(data, list)           # Checking the data type of the response code