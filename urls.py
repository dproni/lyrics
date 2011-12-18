from django.conf.urls.defaults import patterns, include, url
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
    (r'^([0-9])$', artist),
    (r'^([0-9])/([0-9])$', album),
    (r'^([0-9])/([0-9])/([0-9])$', song),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_URL}),
    (r'^albums/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.ALBUMS_URL}),
    (r'^artists/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.ARTISTS_URL}),
                       )
