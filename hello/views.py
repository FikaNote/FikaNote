#!/usr/bin/env python
#coding:utf-8
import requests
from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    episodes = []
    episodes.append({
        'agenda':'あれとこれをそれしました' ,
        'year' : '2015',
        'date' : '05/Jan',
        'title' : 'はじめてのFika',
        'number' : 1
        })
    episodes.append({
        'agenda':'hogeとfugaについて話しました' ,
        'year' : '2015',
        'date' : '09/Jan',
        'title' : '開発者のこれからについて',
        'number' : 2
        })
    return render(request, 'index.html', 
                  {'episodes': episodes
                  } )

def episode(request, number):
    persons = []
    persons.append({'name':'Kosuke Nagano', 'twitter':'gm_kou'})
    persons.append({'name':'Satoshi Nagano', 'twitter':'sassy_watson'})
    shownotes = []
    shownotes.append({'url':'http://www.google.com', 'title':'Google'})
    shownotes.append({'url':'http://www.yahoo.co.jp', 'title':'Yahoo'})
    episode = {
        'agenda':'あれとこれをそれしました' ,
        'year' : '2015',
        'date' : '09/Jan',
        'title' : 'はじめてのFika',
        'number' : 1
        }
    return render(request, 'episode.html', 
                  {'episode': episode, 
                   'shownotes':shownotes, 
                   'persons':persons 
                   } )

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

