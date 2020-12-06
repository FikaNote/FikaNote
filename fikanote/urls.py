from django.conf.urls import include, url, handler404
import app.views
import app.feed
import app.shownote
import app.agenda
import app.agendajson

urlpatterns = [
    url(r'^$', app.views.index, name='index'),
    url(r'^(?P<number>\d+)/$', app.views.episode),
    url(r'^agenda', app.agenda.agenda),
    url(r'^agendajson', app.agendajson.agendajson),
    url(r'^add', app.views.add, name='add'),
    url(r'^shownote', app.shownote.shownote),
    url(r'^feed/', app.feed.feed)
]
