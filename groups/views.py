from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.shortcuts import render, redirect
from django.http import HttpResponse

from members.models import Member
from groups.models import Group, Meeting

import json
from datetime import datetime

def autocomplete_member(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        members = Member.objects.filter(name__icontains = q )[:20]
        results = []
		
        for member in members:
            member_json = {}
            member_json['id'] = member.id
            member_json['label'] = member.name
            member_json['value'] = member.name
            results.append(member_json)

        data = json.dumps(results)
    else:
        data = 'fail'

    mimetype = 'application/json'
    return HttpResponse(data, mimetype)



def search_member_for_group(request, pk):
	""" Receives pk as the key for the Group which we want to add members to """
	context = { 'group_id': pk}
	return render(request, 'groups/search_member_for_group.html', context)



def remove_member_from_group(request, group_id, member_id):
	member = Member.objects.get(pk=member_id)
	group = Group.objects.get(pk=group_id)

	group.members.remove(member)
	group.save()

	context = {'member': member, 'group': group}
	
	return render(request, 'groups/member_removed_from_group.html', context)



def add_member_to_group(request, group_id):
	new_group_member = Member.objects.get(pk=request.POST['member_id'])
	group = Group.objects.get(pk=group_id)
	
	group.members.add(new_group_member)
	group.save()

	context = {'new_group_member': new_group_member.name, 'group_name': group.name}

	return render(request, 'groups/member_added_to_group_sucess.html', context)



def register_meeting(request, group_id):
	group = Group.objects.get(pk=group_id)
	group_members = group.members.all()
	context = {'group': group, 'group_members': group_members}

	return render(request, 'groups/register_meeting.html', context)



def submit_meeting(request, group_id):
	present_members_ids = request.POST.getlist('members')
	present_members = []

	for member_id in present_members_ids:
		present_members.append(Member.objects.get(pk=member_id))

	group = Group.objects.get(pk=group_id)
	comments = request.POST['comments']
	meeting_type = request.POST['type']
	date = datetime.strptime(request.POST['date'], "%d/%m/%Y").strftime("%Y-%m-%d")

	meeting = Meeting()

	group.meeting_set.add(meeting)

	meeting.group = group
	meeting.type = meeting_type
	meeting.comments = comments
	meeting.date = date
	meeting.members_who_attended = present_members

	meeting.save()

	context = {}

	return render(request, 'groups/submit_meeting.html', context)



class GroupListView(ListView):
	template_name = 'groups/list.html'
	context_object_name = 'group_list'

	def get_queryset(self):
		""" Return all registered members """
		return Group.objects.all()



class GroupDetailView(DetailView):
	model = Group
	template_name = 'groups/detail.html'

	def get_context_data(self, **kwargs):
		context = super(GroupDetailView, self).get_context_data(**kwargs)
		context["group_members"] = context['group'].members.all()
		context["last_meetings"] = Meeting.objects.filter(group=context['group']).order_by('-date')[:5]
		
		return context



class GroupCreateView(CreateView):
	model = Group
	template_name = 'groups/form.html'
	fields = ['name', 'leader']
	success_url = reverse_lazy('groups:group_list')



class GroupUpdateView(UpdateView):
	model = Group
	template_name = 'groups/form.html'
	fields = ['name', 'leader']
	success_url = reverse_lazy('groups:group_list')



class GroupDeleteView(DeleteView):
	model = Group
	template_name = 'groups/confirm_delete.html'
	success_url = reverse_lazy('groups:group_list')