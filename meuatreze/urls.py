from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from meuatreze import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'meuatreze.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^pessoal/', views.personal, name='personal'),
    url(r'^members/', include('members.urls', namespace='members')),
    url(r'^groups/', include('groups.urls', namespace='groups')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'logged_out.html'}),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^$', views.index, name='index'),
)
