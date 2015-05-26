from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    # Examples:
    url(r'^$', TemplateView.as_view(template_name="repository/index.html")),
    # url(r'^blog/', include('blog.urls')),
    url(r'^repository/', include('repository.urls', namespace="repository")),
    url(r'^registration/', include('registration.urls', namespace="registration")),
    url(r'^admin/', include(admin.site.urls)),
]
