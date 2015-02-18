from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import hello.views
import hello.feed

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gettingstarted.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', hello.views.index, name='index'),
    url(r'^(?P<number>\d+)', hello.views.episode, name='episode'),
    url(r'^agenda', hello.views.agenda, name='agenda'),
    url(r'^add', hello.views.add, name='add'),
    url(r'^feed/', hello.feed.feed, name='feed'),
    url(r'^admin/', include(admin.site.urls)),


)
