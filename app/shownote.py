#!/usr/bin/env python
#coding:utf-8

from django.http import Http404,HttpResponseRedirect
from app.models import FikanoteDB, AgendaDB, Shownote
from shownoteform import ShownoteForm
from agendaform import AgendaForm
from django.shortcuts import render
import datetime

def shownote(request):
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
