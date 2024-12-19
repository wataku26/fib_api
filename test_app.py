import unittest
from app import app

class FibonacciAPITestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_valid_request(self):
        response = self.app.get('/fib?n=10')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['result'], 55)

    def test_missing_parameter(self):
        response = self.app.get('/fib')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['message'], "Parameter 'n' is required.")

    def test_negative_input(self):
        response = self.app.get('/fib?n=-5')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['message'], "The number must be a positive integer.")

    def test_invalid_input(self):
        response = self.app.get('/fib?n=abc')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['message'], "invalid literal for int() with base 10: 'abc'")

if __name__ == '__main__':
    unittest.main()
