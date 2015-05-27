import unittest
from django.test.client import Client
from django.db import models
from app.models import FikanoteDB

class EpisodeTest(unittest.TestCase):
    def setUp(self):
        # unittest requires to create Client everytime
        self.client = Client()

    def test_get_episode(self):
        episodes = FikanoteDB.objects.order_by('-date')
        for e in episodes:
            target = "/" + str(e.number)
            # GET request 
            response = self.client.get(target)
            # expect to return 200 OK 
            self.assertEqual(response.status_code, 200)
