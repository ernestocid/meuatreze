from django.conf.urls import patterns, url
from members import views
from django.contrib.auth.decorators import login_required, permission_required


urlpatterns = patterns('',
    url(r'^$', login_required(views.MemberListView.as_view()), name='member_list'),
    url(r'^(?P<pk>\d+)/$', login_required(views.MemberDetailView.as_view()), name='member_detail'),
    url(r'^add/$', login_required(views.MemberCreateView.as_view()), name='member_add'),
    url(r'^(?P<pk>\d+)/update/$', login_required(views.MemberUpdateView.as_view()), name='member_update'),
    url(r'^(?P<pk>\d+)/delete/$', login_required(views.MemberDeleteView.as_view()), name='member_delete'),
)