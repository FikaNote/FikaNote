from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static


from django.contrib import admin
admin.autodiscover()

import app.views
import app.feed
import app.shownote
import app.agenda
import app.agendajson
 
urlpatterns = [
    # Examples:
    # url(r'^$', 'fikanote.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', app.views.index, name='index'),
    url(r'^(?P<number>\d+)/$', app.views.episode),
    url(r'^agenda', app.agenda.agenda),
    url(r'^agendajson', app.agendajson.agendajson),
    url(r'^add', app.views.add, name='add'),
    url(r'^shownote', app.shownote.shownote),
    url(r'^feed/', app.feed.feed),
    url(r'^admin/', include(admin.site.urls)),
]

