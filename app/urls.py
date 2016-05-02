from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^menu', views.menu, name='menu'),
    url(r'^about', views.about, name='about'),
]
