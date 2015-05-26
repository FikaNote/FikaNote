import unittest
from django.test.client import Client
from django.db import models
from app.models import FikanoteDB
import feedparser

class FeedTest(unittest.TestCase):
    def setUp(self):
        # unittest requires to create Client everytime
        self.client = Client()
        
    def test_get_feed(self):
        # GET request 
        response = self.client.get('/feed/')
        # expect to return 200 OK 
        self.assertEqual(response.status_code, 200)

    def test_count_feed(self):
        count = FikanoteDB.objects.order_by('-date').count()
        self.assertGreater(count, 0)

    def test_same_count_feed(self):
        response = self.client.get('/feed/')
        rss = feedparser.parse(response.content)
        if rss.bozo:
            raise rss.bozo_exception
        feed_entries = len(rss.entries)
        db_count = FikanoteDB.objects.order_by('-date').count()
        self.assertEqual(db_count, feed_entries)
