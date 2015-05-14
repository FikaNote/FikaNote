#!/usr/bin/env python
#coding:utf-8

from agendaform import AgendaForm
from django.shortcuts import render
import requests
from django.http import HttpResponse,Http404,QueryDict
from .models import FikanoteDB, AgendaDB, Shownote
import urllib2
from BeautifulSoup import BeautifulSoup
import json
import datetime

def agenda(request):
    if request.method == 'GET': 
        agendas = AgendaDB.objects().order_by('-date')
        form = AgendaForm() 
        return render(request, 'agenda.html', 
                      {'agendas': agendas, 
                       'form': form
                       } )

    elif request.method == 'POST': 
        form = AgendaForm(request.POST) 
        if form.is_valid(): 
            url = form.cleaned_data['url']
            req = urllib2.Request(url, None, headers = { 'User-Agent' : 'Mozilla/5.0' })
            soup = BeautifulSoup(urllib2.urlopen(req))
            title = soup.title.string
            AgendaDB(url=url, title=title, date=datetime.datetime.utcnow()).save()

            response = json.dumps({'status':'success', 'url':url, 'title':title})  # convert to JSON
        else:
            response = json.dumps({'status':'fail'})  # convert to JSON

        return HttpResponse(response, content_type="application/json")

    elif request.method == 'DELETE': 
        delete = QueryDict(request.body)
        id = delete.get('id')
        if id :
            AgendaDB.objects.filter(id__exact=id).delete()
            response = json.dumps({'status':'success'})  # convert to JSON
        else:
            response = json.dumps({'status':'fail'})  # convert to JSON
        return HttpResponse(response, content_type="application/json")

    else:
        raise Http404

