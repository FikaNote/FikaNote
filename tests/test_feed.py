import unittest
from django.test.client import Client

class FeedTest(unittest.TestCase):
    def setUp(self):
        # unittest requires to create Client everytime
        self.client = Client()

    def test_get_feed(self):
        # GET request 
        response = self.client.get('/feed/')

        # expect to return 200 OK 
        self.failUnlessEqual(response.status_code, 200)

