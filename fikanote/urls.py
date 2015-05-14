from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import app.views
import app.feed
import app.shownote
import app.agenda
 
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fikanote.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', app.views.index, name='index'),
    url(r'^(?P<number>\d+)', app.views.episode, name='episode'),
    url(r'^agenda', app.agenda.agenda, name='agenda'),
    url(r'^add', app.views.add, name='add'),
    url(r'^shownote', app.shownote.shownote, name='shownote'),
    url(r'^feed/', app.feed.feed, name='feed'),
    url(r'^admin/', include(admin.site.urls)),


)
