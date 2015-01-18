# Django Imports
from django.conf.urls import patterns, include, url
from django.contrib import admin
from stream.views import view_streams
from stream.views import view_stream_for_user
import settings


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^stream/$', view_streams),
    url(r'^stream/(?P<user_id>[^/]+)/$', view_stream_for_user),
)