# !/usr/bin/env python
# coding:utf-8


from .agendaform import AgendaForm
from django.shortcuts import render
from django.http import HttpResponse, Http404, QueryDict
from app.models import AgendaDB
import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup
import json
import datetime
import http.client
from PyPDF2 import PdfFileReader

def agenda(request):
    if request.method == 'GET':
        agendas = AgendaDB.objects().order_by('-date')
        form = AgendaForm()
        return render(request, 'agenda.html',
                      {'agendas': agendas,
                       'form': form
                       })

    elif request.method == 'POST':
        form = AgendaForm(request.POST)
        if not form.is_valid():
            response = json.dumps({'status': 'fail'})  # convert to JSON
            return HttpResponse(response, content_type="application/json")
        try:
            url = form.cleaned_data['url']
            title = agendaGetTitle(url)
        except http.client.BadStatusLine as e:
            title = "UNNAMED URL"

        agendaItem = AgendaDB(url=url,
                              title=title,
                              date=datetime.datetime.utcnow())
        agendaItem.save()
        
        response = json.dumps({'status': 'success',
                               'url': url,
                               'title': title,
                               'id': str(agendaItem.id)
        })  # convert to JSON
        return HttpResponse(response, content_type="application/json")
    
    elif request.method == 'DELETE':
        delete = QueryDict(request.body)
        delete_id = delete.get('id')
        if delete_id:
            AgendaDB.objects.filter(id__exact=delete_id).delete()
            response = json.dumps({'status': 'success'})  # convert to JSON
        else:
            response = json.dumps({'status': 'fail'})  # convert to JSON
        return HttpResponse(response, content_type="application/json")
            
    else:
            raise Http404


def agendaGetTitle(url):
    req = urllib.request.Request(url, None)
    req.add_header("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36")
    req.add_header("Accept", "text/html,application/xhtml+xml,application/xml")
    req.add_header("Accept-Language", "ja")
    req.add_header("Accept-Encoding", "identity")
    req.add_header("Pragma", "no-cache")
    res = urllib.request.urlopen(req)
    mime = res.getheader('content-type')

    if mime == 'application/pdf':
        # save to temporal file
        f = open('workfile.pdf', 'wb')
        f.write(res.read())
        f.close()
        # open pdf file
        input = PdfFileReader(open('workfile.pdf', 'rb'))
        title = input.getDocumentInfo().title
    else:
        soup = BeautifulSoup(res, "html.parser")
        title = soup.title.string

    return title
