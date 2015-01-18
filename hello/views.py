#!/usr/bin/env python
#coding:utf-8
import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from .models import Greeting

import pymongo
from pymongo import ASCENDING, DESCENDING

from agendaform import AgendaForm

MONGODB_URI = 'mongodb://fikakou:0US3ZKxV@ds029811.mongolab.com:29811/fikanotedb' 

# Create your views here.
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
    fikanote = db['agendadb']
    agendas = fikanote.find().sort("date", pymongo.DESCENDING)
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
            print(form)
        else:
            print(form)            
                
    return HttpResponseRedirect('/agenda/') 

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

