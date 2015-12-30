from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from members.models import Member
from groups.models import Group


class MemberListView(ListView):
	template_name = 'members/list.html'
	context_object_name = 'all_members'

	def get_queryset(self):
		""" Return all registered members """
		return Member.objects.all()


class MemberDetailView(DetailView):
	model = Member
	template_name = 'members/detail.html'

	def get_context_data(self, **kwargs):
		context = super(MemberDetailView, self).get_context_data(**kwargs)
		context["member_groups"] = context['member'].member_groups.all()
		context["leader_of_groups"] = Group.objects.filter(leader=context['member'])

		return context


class MemberCreateView(CreateView):
	model = Member
	template_name = 'members/form.html'
	fields = ['name', 'email', 'is_leader', 'is_department_leader']
	success_url = reverse_lazy('members:member_list')


class MemberUpdateView(UpdateView):
	model = Member
	template_name = 'members/form.html'
	fields = ['name', 'email', 'is_leader', 'is_department_leader']
	success_url = reverse_lazy('members:member_list')


class MemberDeleteView(DeleteView):
	model = Member
	template_name = 'members/confirm_delete.html'
	success_url = reverse_lazy('members:member_list')



