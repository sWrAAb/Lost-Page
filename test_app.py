import unittest
from  app import app
from flask_pymongo import PyMongo

class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        # Test for a link to books.html
        self.assertIn(b'href="/books"', response.data)
        # Test for a home page link image source
        self.assertIn(b'src="https://cdn.wallpaperdirect.com/asset/img/product/143795/tiled/albany-fashion-library-black-and-white-wallpaper-tiled-143795.jpg"', response.data)


    def test_books_page(self):
        response = self.app.get('/books')
        self.assertEqual(response.status_code, 200)
        # Check for a piece of text or HTML element you expect in books.html
        self.assertIn(b'Books', response.data)


    def test_search_function(self):
        response = self.app.get('/search?query=bu')
        self.assertEqual(response.status_code, 200)
        # Check that the response contains the expected books or message for the search term
        self.assertIn(b'bu', response.data)

    def test_add_book(self):
        response = self.app.post('/insert_book', data=dict(
            title="Test Book",
            author="Test Author",
            year="2021",
            genre="Test Genre",
            cover_img="url/to/test/image"
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        # Verify the book was added, might need to query the test database

if __name__ == "__main__":
    unittest.main()