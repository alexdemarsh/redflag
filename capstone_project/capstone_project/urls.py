from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'capstone_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^repository/', include('repository.urls', namespace="repository")),
    url(r'^registration/', include('registration.urls', namespace="registration")),
    url(r'^admin/', include(admin.site.urls)),
]
