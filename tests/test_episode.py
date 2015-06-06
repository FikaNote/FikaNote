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
            target = "/" + str(number) + "/"
            # GET request 
            response = self.client.get(target)
            # expect to return 200 OK 
            self.assertEqual(response.status_code, 200)

    def test_get_episode_incorrect_num(self):
        target = "/" + str(len(self.episodes)+1) + "/" # +1 for incorrect number.
        expectedPath = '/'
        # GET request 
        response = self.client.get(target)
        self.assertEqual(response.status_code, 301)
        self.assertEqual(urlparse(response['Location']).path, expectedPath)

    def test_get_episode_incorrect_string1(self):
        target = "/a12/" 
        # GET request 
        response = self.client.get(target)
        self.assertEqual(response.status_code, 404)

    def test_get_episode_incorrect_string2(self):
        target = "/12a/" 
        # GET request 
        response = self.client.get(target)
        self.assertEqual(response.status_code, 404)

    def test_get_episode_incorrect_string3(self):
        target = "/hoge/" 
        # GET request 
        response = self.client.get(target)
        self.assertEqual(response.status_code, 404)

        
