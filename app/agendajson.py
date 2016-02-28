# !/usr/bin/env python
# coding:utf-8


from django.http import HttpResponse, Http404
from app.models import AgendaDB
import json


def agendajson(request):
    if request.method == 'POST':
        # need to handle CSRF
        # how?

        j = json.loads(request.body)
        title = j['title']
        url = j['url']
        response = json.dumps({'status': 'success',
                               'url': url,
                               'title': title})
    else:
        response = json.dumps({'status': 'fail'})
        return HttpResponse(response, content_type="application/json")
