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
    persons = []
    persons.append({'name':'Kosuke Nagano', 'twitter':'gm_kou', 
                    'avatar':'https://pbs.twimg.com/profile_images/780617517/IMG_0151_400x400.JPG'})
    persons.append({'name':'Satoshi Nagano', 'twitter':'sassy_watson',
                    'avatar':'https://pbs.twimg.com/profile_images/1197190603/bird_bigger_400x400.png'})
    shownotes = []
    shownotes.append({'id':1, 'url':'http://www.google.com', 'title':'Google', 'introducer':'gm_kou' })
    shownotes.append({'id':2, 'url':'http://www.yahoo.co.jp', 'title':'Yahoo', 'introducer':'sassy_watson' })
    episode = {
        'agenda':'あれとこれをそれしました' ,
        'year' : '2015',
        'date' : '09/Jan',
        'title' : 'はじめてのFika',
        'number' : 1,
        'person' : ['gm_kou', 'sassy_watson'],
        'shownote' : [1, 2]
        }
    return render(request, 'episode.html', 
                  {'episode': episode, 
                   'shownotes':shownotes, 
                   'persons':persons 
                   } )

def agenda(request):
    agendas = []
    agendas.append({'id':1, 'url':'http://www.google.com', 'title':'Google', 'introducer':'gm_kou' })
    agendas.append({'id':2, 'url':'http://www.yahoo.co.jp', 'title':'Yahoo', 'introducer':'sassy_watson' })
    context = RequestContext(request, {'agendas':agendas})
    return render_to_response("agenda.html", context)


def add(request):
    if request.method == 'POST':
        response_data = {}
        response_data['result'] = 'success'
        response_data['message'] = 'success'
        return HttpResponse(json.dumps(response_data), content_type="application/json")
    else:
        response_data = {}
        response_data['result'] = 'failed'
        response_data['message'] = 'not support this method'
        return HttpResponse(json.dumps(response_data), content_type="application/json")

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

