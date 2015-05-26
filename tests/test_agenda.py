import unittest
from django.test.client import Client
from django.db import models
from app.models import AgendaDB
import feedparser

class AgendaTest(unittest.TestCase):
    def setUp(self):
        # unittest requires to create Client everytime
        self.client = Client()
        
    def test_get_agenda(self):
        # GET request 
        response = self.client.get('/agenda/')
        # expect to return 200 OK 
        self.assertEqual(response.status_code, 200)

    def test_count_agenda(self):
        count = AgendaDB.objects.order_by('-date').count()
        self.assertGreater(count, 0)

