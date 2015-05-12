#!/usr/bin/env python
#coding:utf-8
import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import QueryDict
from django.shortcuts import render_to_response
from django.template import RequestContext

from .models import Greeting
from .models import FikanoteDB, AgendaDB, Shownote

from agendaform import AgendaForm
from shownoteform import ShownoteForm
import urllib2
from BeautifulSoup import BeautifulSoup
import datetime

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

def agenda(request):
    import json
    from django.http import HttpResponse,Http404

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

def shownote(request):
    import json
    from django.http import HttpResponse,Http404

    if request.method == 'GET': 
        agendas = AgendaDB.objects().order_by('-date')
        return render(request, 'edit_shownote.html', 
                      {'agendas': agendas 
                       , 'agendaform': AgendaForm()
                       , 'shownoteform': ShownoteForm() 
                       } )

    elif request.method == 'POST': 
        form = ShownoteForm(request.POST) 
        if form.is_valid(): 
            number = FikanoteDB.objects().count()+1
            # add to shownote
            shownotes = []
            list_title = request.POST.getlist('agenda_title')
            list_url = request.POST.getlist('agenda_url')
            list_id = request.POST.getlist('agenda_id')
            for i in range(len(list_title)):
                shownotes.append(Shownote(title=list_title[i], url=list_url[i]))
            FikanoteDB(number = number
                       , title=form.cleaned_data['title']
                       , person=form.cleaned_data['person'].split(",")
                       , agenda=form.cleaned_data['agenda']
                       , date=datetime.datetime.utcnow()
                       , shownotes=shownotes
                       ).save()
            # delete id's item from agendadb
            for i in range(len(list_id)):
                AgendaDB.objects.filter(id__exact=list_id[i]).delete()

        return HttpResponseRedirect('/') 
        
    else:
        raise Http404

def add(request):
    return HttpResponseRedirect('/agenda/') 


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

