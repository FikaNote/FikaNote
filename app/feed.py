#!/usr/bin/env python
#coding:utf-8
from django.http import HttpResponse
from app.models import FikanoteDB
from django.utils import feedgenerator

def feed(request):
    assert request.method == 'GET',  "error on request method"

    feed=feedgenerator.Rss201rev2Feed(
        title='FikaNote'
        , link='https://fikanote.herokuapp.com/'
        , description='Talking about Tech, Software Development and Gadgets with Coffee.'
        , language='ja-jp'
        )

    episodes = FikanoteDB.objects.order_by('-date')
    for episode in episodes:
        url = 'https://fikanote.herokuapp.com/%d/' % episode.number
        feed.add_item(
            title='FikaNote %d: %s' % (episode.number ,episode.title)
            , link=url
            , author_email='Kosuke Nagano'
            , description=episode.agenda
            , pubdate=episode.date
            )

    result=feed.writeString('utf-8')
    return HttpResponse(result, content_type="text/xml; charset=utf-8")



