#!/usr/bin/env python
#coding:utf-8

from django.shortcuts import render
from django.http import HttpResponse,Http404,QueryDict
from app.models import AgendaDB
import urllib2
from BeautifulSoup import BeautifulSoup
import json
import datetime
import httplib

def agendajson(request):
    if request.method == 'POST':
        # need to handle CSRF
        # how?
        
        j = json.loads(request.body)
        title = j['title']
        url = j['url']
        # AgendaDB(url=url, title=title, date=datetime.datetime.utcnow()).save()
        response = json.dumps({'status':'success', 'url':url, 'title':title})  # convert to JSON
    else:
        response = json.dumps({'status':'fail'})  # convert to JSON
        return HttpResponse(response, content_type="application/json")
    
    
