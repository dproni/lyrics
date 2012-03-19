from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib import admin
from main.views import *
from main.forms import *
from haystack.query import SearchQuerySet
from haystack.views import SearchView

admin.autodiscover()
sqs = SearchQuerySet()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    (r'^$', main),
    (r'^add/', add),
    (r'^contact/', contact),
    (r'^([A-Z]{1})/', letter),
    (r'^number/$', number),
    (r'^(\d{1,10})/$', artist),
    (r'^(\d{1,10})/(\d{1,10})/$', song),
#    (r'^(\d{1,10})/(\d{1,10})/$', album), #TODO should be with tag
#    (r'^(\d{1,10})/(\d{1,10})/(\d{1,10})/$', song), # TODO goes to album
    (r'^ajax/(\d{1,10})/(\d{1,10})/(\d{1,10})/$', ajax_lyrics),
    (r'^ajax_song_info/(\d{1,10})/(\d{1,10})/(\d{1,10})/$', ajax_song_info),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_URL}),
    (r'^albums/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.ALBUMS_URL}),
    (r'^artists/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.ARTISTS_URL}),
    (r'^search/', SearchView(
        template='search/search.html',
        searchqueryset=sqs,
        form_class=SimpleSearchForm,
        results_per_page=None
    )),
)