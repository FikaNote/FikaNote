#!/usr/bin/env python
#coding:utf-8

from .agendaform import AgendaForm
from django.shortcuts import render
from django.http import HttpResponse,Http404,QueryDict
from app.models import AgendaDB
import urllib
from bs4 import BeautifulSoup
import json
import datetime
import http.client

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
            try:
                url = form.cleaned_data['url']
                req = urllib.Request(url, None, headers = { 'User-Agent' : 'Mozilla/5.0' })
                soup = BeautifulSoup(urllib.urlopen(req))
                title = soup.title.string

            except http.client.BadStatusLine as e:
                title = "UNNAMED URL"

            agendaItem = AgendaDB(url=url, title=title, date=datetime.datetime.utcnow())
            agendaItem.save()

            response = json.dumps({'status':'success', 'url':url, 'title':title, "id":str(agendaItem.id)})  # convert to JSON
        else:
            response = json.dumps({'status':'fail'})  # convert to JSON

        return HttpResponse(response, content_type="application/json")

    elif request.method == 'DELETE':
        delete = QueryDict(request.body)
        delete_id = delete.get('id')
        if delete_id :
            AgendaDB.objects.filter(id__exact=delete_id).delete()
            response = json.dumps({'status':'success'})  # convert to JSON
        else:
            response = json.dumps({'status':'fail'})  # convert to JSON
        return HttpResponse(response, content_type="application/json")

    else:
        raise Http404
