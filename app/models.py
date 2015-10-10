from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)

# MongoDB

import mongoengine
from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import *

MONGODB_URI = 'mongodb://fikakou:0US3ZKxV@ds029811.mongolab.com:29811/fikanotedb'

mongoengine.connect('fikanotedb', host=MONGODB_URI)

class Shownote(EmbeddedDocument):
    url = URLField()
    title = StringField()

class FikanoteDB(Document):
    title = StringField()
    number = IntField()
    person = ListField(StringField())
    agenda = StringField()
    date = DateTimeField()
    shownotes = EmbeddedDocumentListField(Shownote)
    
    meta = {'collection': 'fikanotedb'}

class AgendaDB(Document):
    url = URLField()
    title = StringField()
    date = DateTimeField()
    
    meta = {'collection': 'agendadb'}
