import unittest
from tools import add, multiply
from agent import Response

class TestTools(unittest.TestCase):
    def test_add(self):
        result = add(5, 3)
        self.assertEqual(result, 8)
    
    def test_multiply(self):
        result = multiply(4, 7)
        self.assertEqual(result, 28)

class TestResponse(unittest.TestCase):
    def test_response_model(self):
        response = Response(text="Hello", tools_used="none")
        self.assertEqual(response.text, "Hello")
        self.assertEqual(response.tools_used, "none")

if __name__ == '__main__':
    unittest.main()