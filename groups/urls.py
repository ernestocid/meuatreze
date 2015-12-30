from django.conf.urls import patterns, url
from groups import views
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = patterns('',
    url(r'^$', login_required(views.GroupListView.as_view()), name='group_list'),
    url(r'^(?P<pk>\d+)/$', login_required(views.GroupDetailView.as_view()), name='group_detail'),
    url(r'^add/$', login_required(views.GroupCreateView.as_view()), name='group_add'),
    url(r'^autocomplete_member/', login_required(views.autocomplete_member), name='autocomplete_member'),
    url(r'^(?P<pk>\d+)/update/$', login_required(views.GroupUpdateView.as_view()), name='group_update'),
    url(r'^(?P<pk>\d+)/delete/$', login_required(views.GroupDeleteView.as_view()), name='group_delete'),
    url(r'^(?P<pk>\d+)/search_member_for_group/$', login_required(views.search_member_for_group), name='search_member_for_group'),
    url(r'^(?P<group_id>\d+)/add_member_to_group/$', login_required(views.add_member_to_group), name='add_member_to_group'),
    url(r'^(?P<group_id>\d+)/register_meeting/$', login_required(views.register_meeting), name='register_meeting'),
    url(r'^(?P<group_id>\d+)/submit_meeting/$', login_required(views.submit_meeting), name='submit_meeting'),
    url(r'^(?P<group_id>\d+)/remove_member_from_group/(?P<member_id>\d+)$', login_required(views.remove_member_from_group), name='remove_member_from_group'),
)