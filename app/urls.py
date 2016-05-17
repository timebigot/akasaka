from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls import patterns

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^menu', views.menu, name='menu'),
    url(r'^about', views.about, name='about'),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^img/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))
