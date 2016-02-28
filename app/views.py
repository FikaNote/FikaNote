# !/usr/bin/env python
# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect
from app.models import Greeting
from app.models import FikanoteDB


def index(request):
    episodes = FikanoteDB.objects.order_by('-date')
    return render(request, 'index.html',
                  {'episodes': episodes
                   })


def episode(request, number):
    episode = FikanoteDB.objects(number=int(number)).first()
    if episode is None:
        return HttpResponsePermanentRedirect('/')

    person = episode['person']
    shownotes = episode['shownotes']

    return render(request, 'episode.html',
                  {'episode': episode,
                   'person': person,
                   'shownotes': shownotes,
                   })


def add(request):
    return HttpResponseRedirect('/agenda/')
