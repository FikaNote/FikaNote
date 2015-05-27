import unittest
from django.test.client import Client

class HomeTest(unittest.TestCase):
    def setUp(self):
        # unittest requires to create Client everytime
        self.client = Client()
        
    def test_get_home(self):
        # GET request 
        response = self.client.get('/')
        # expect to return 200 OK 
        self.assertEqual(response.status_code, 200)
