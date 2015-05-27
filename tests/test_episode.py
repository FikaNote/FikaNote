import unittest
from django.test.client import Client
from django.db import models
from app.models import FikanoteDB
from urlparse import urlparse

class EpisodeTest(unittest.TestCase):
    def setUp(self):
        # unittest requires to create Client everytime
        self.client = Client()
        self.episodes = FikanoteDB.objects.order_by('-date')

    def test_get_episode(self):
        for number in range(1 , len(self.episodes)):
            target = "/" + str(number)
            # GET request 
            response = self.client.get(target)
            # expect to return 200 OK 
            self.assertEqual(response.status_code, 200)

    def test_get_episode_incorrect_num(self):
        target = "/" + str(len(self.episodes)+1)
        expectedPath = '/'
        # GET request 
        response = self.client.get(target)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(urlparse(response['Location']).path, expectedPath)
        
