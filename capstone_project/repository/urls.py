from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<data_id>[0-9]+)/$', views.datum, name='datum'),
    # url (r'^upload/$', views.upload_csv, name="upload"),
    url (r'^upload_file/$', views.upload_file, name="upload_file"),
]