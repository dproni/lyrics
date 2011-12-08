from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib import admin
from main.views import *

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       (r'^$', info),
                       (r'^add/', add),
                       (r'^([A-Z]{1})/', search),
                       (r'^artist/(.*)$', artist),
                       (r'^~/(.*)/(.*)/(.*)$', song),
                       (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_URL}),
                       )
