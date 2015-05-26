import unittest
from django.test.client import Client
from django.db import models

class ShownoteTest(unittest.TestCase):
    def setUp(self):
        # unittest requires to create Client everytime
        self.client = Client()
        
    def test_get_shownote(self):
        # GET request 
        response = self.client.get('/shownote/')
        # expect to return 200 OK 
        self.assertEqual(response.status_code, 200)

