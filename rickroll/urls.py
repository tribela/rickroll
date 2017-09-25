from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.create_new, name='create_new'),
    url(r'^(?P<id_str>.*)/preview', views.preview, name='preview'),
    url(r'^(?P<id_str>[^/]+)/?$', views.link_view, name='link_view'),
]
