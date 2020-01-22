from app import app
import unittest


class FlaskTestCase(unittest.TestCase):

        
    def test_home(self):
        """Ensure the flask was setup correctly"""
        tester=app.test_client(self)
        response=tester.get('/home', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        
        
    def test_books(self):
        """Ensure the flask was setup correctly"""
        tester=app.test_client(self)
        response=tester.get('/books', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        
    
    def test_home_page_load(self):
        """Ensure home page loads correctly"""
        tester=app.test_client(self)
        response=tester.get('/home', content_type='html/text')
        self.assertTrue(b'The Lost Page' in response.data)
    
    
    def test_book_page_load(self):
        """Ensure book page loads correctly"""
        tester=app.test_client(self)
        response=tester.get('/books', content_type='html/text')
        self.assertTrue(b'Books' in response.data)
        
    
    def test_add_book(self):
        """Add book and check new book shows after redirect"""
        tester=app.test_client(self)
        response=tester.get('/add_book', data=dict(title= 'Around the World in Eighty Days'), 
        follow_redirects=True)
        self.assertIn(b'Adventure', response.data)    
        






if __name__ == '__main__':
    unittest.main()