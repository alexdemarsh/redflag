from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from repository import views


urlpatterns = [
    # Examples:
    url(r'^$', views.index, name='index'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^repository/', include('repository.urls', namespace="repository")),
    url(r'^registration/', include('registration.urls', namespace="registration")),
    url(r'^admin/', include(admin.site.urls)),
    ]