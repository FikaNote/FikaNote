#!/usr/bin/env python
#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Greeting
from .models import FikanoteDB

def index(request):
    episodes = FikanoteDB.objects.order_by('-date')
    return render(request, 'index.html', 
                  {'episodes': episodes
                   } )

def episode(request, number):
    episode = FikanoteDB.objects(number=int(number)).first()
    if episode is not None:
        person = episode['person']
        shownotes = episode['shownotes']
    else:
        episode = {'title': 'no such episode'}
        person = []
        shownotes = []

    return render(request, 'episode.html', 
                  {'episode': episode, 
                   'person' : person,
                   'shownotes' : shownotes,
                   } )


def add(request):
    return HttpResponseRedirect('/agenda/') 


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

