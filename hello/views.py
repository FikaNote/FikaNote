#!/usr/bin/env python
#coding:utf-8
import requests
from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    r = requests.get('http://httpbin.org/status/418')
    print r.text
    return HttpResponse('<pre>' + r.text + '</pre>')

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
                   'persons':persons, 
                   } )
    r = requests.get('http://httpbin.org/status/418')
    print r.text
    return HttpResponse('<pre>' + r.text + '</pre>')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

