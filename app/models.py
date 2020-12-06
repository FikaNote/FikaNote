from django.db import models
import mongoengine
from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import *

import os

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)

MONGODB_USER = os.environ.get("DATABASE_USER")
MONGODB_PASSWORD = os.environ.get("DATABASE_PASSWORD")
MONGODB_URI = "mongodb+srv://" + MONGODB_USER + ":" + MONGODB_PASSWORD + "@fikanotedb.ltkpy.mongodb.net/fikanotedb?retryWrites=true&w=majority"
mongoengine.connect('fikanotedb', host=MONGODB_URI)

class Shownote(EmbeddedDocument):
    url = URLField()
    title = StringField()
    date = DateTimeField()


class FikanoteDB(Document):
    title = StringField()
    number = IntField()
    person = ListField(StringField())
    agenda = StringField()
    date = DateTimeField()
    shownotes = ListField(EmbeddedDocumentField(Shownote))

    meta = {'collection': 'fikanotedb'}


class AgendaDB(Document):
    url = URLField()
    title = StringField()
    date = DateTimeField()

    meta = {'collection': 'agendadb'}
