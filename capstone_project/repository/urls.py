from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<data_id>[0-9]+)/$', views.datum, name='datum'),
    url (r'^upload/$', views.upload, name="upload"),
]