from django.conf.urls.defaults import patterns, include, url
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib import admin
from main.views import *

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
    (r'^$', main),
    (r'^add/', add),
    (r'^contact/', contact),
    (r'^([A-Z]{1})/', letter),
    (r'^(\d{1,10})/$', artist),
    (r'^(\d{1,10})/(\d{1,10})/$', album),
    (r'^(\d{1,10})/(\d{1,10})/(\d{1,10})/$', song),
    (r'^(\d{1,10})/(\d{1,10})/(\d{1,10})/$', ajax_lyrics),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_URL}),
    (r'^albums/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.ALBUMS_URL}),
    (r'^artists/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.ARTISTS_URL}),
                       )
