#!/usr/bin/env python
#coding:utf-8
import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from .models import Greeting

import pymongo
from pymongo import ASCENDING, DESCENDING

from agendaform import AgendaForm
import urllib2
from BeautifulSoup import BeautifulSoup
import datetime

MONGODB_URI = 'mongodb://fikakou:0US3ZKxV@ds029811.mongolab.com:29811/fikanotedb' 

def index(request):
    client = pymongo.MongoClient(MONGODB_URI)
    db = client.get_default_database()
    fikanote = db['fikanotedb']
    episodes = fikanote.find().sort("date", pymongo.DESCENDING)
    client.close()
    return render(request, 'index.html', 
                  {'episodes': episodes
                   } )

def episode(request, number):
    client = pymongo.MongoClient(MONGODB_URI)
    db = client.get_default_database()
    fikanote = db['fikanotedb']
    episodes = fikanote.find({"number":int(number)})
    if episodes.count() == 0:
        episode = []
        episode.append({'title': 'no such episode'})
    else:
        episode = episodes[0]
    person = episode['person']
    shownotes = episode['shownotes']

    return render(request, 'episode.html', 
                  {'episode': episode, 
                   'person' : person,
                   'shownotes' : shownotes,
                   } )

def agenda(request):
    client = pymongo.MongoClient(MONGODB_URI)
    db = client.get_default_database()
    agendadb = db['agendadb']
    agendas = agendadb.find().sort("date", pymongo.DESCENDING)
    client.close()

    form = AgendaForm() 

    return render(request, 'agenda.html', 
                  {'agendas': agendas, 
                   'form': form
                   } )

def add(request):
    if request.method == 'POST': 
        form = AgendaForm(request.POST) 
        if form.is_valid(): 
            url = form.cleaned_data['url']
            soup = BeautifulSoup(urllib2.urlopen(url))
            title = soup.title.string

            client = pymongo.MongoClient(MONGODB_URI)
            db = client.get_default_database()
            agendadb = db['agendadb']
            agendadb.insert({'url': url, 
                             'title':title,
                             'date': datetime.datetime.utcnow()})
            client.close()

    return HttpResponseRedirect('/agenda/') 

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

