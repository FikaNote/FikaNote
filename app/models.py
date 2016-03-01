from django.db import models
import mongoengine
from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import *


# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)


MONGODB_URI = 'mongodb://fikakou:0US3ZKxV@ds029811.mlab.com:29811/fikanotedb'
# MONGODB_URI = 'mongodb://fikakou:0US3ZKxV@ds031314-a0.mongolab.com:31314,ds031314-a1.mongolab.com:31314/fikanotedb26?replicaSet=rs-ds031314'
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
