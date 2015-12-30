from django.shortcuts import render, redirect
from members.models import Member
from groups.models import Group

def index(request):
	if request.user.is_authenticated():
		members_count = Member.objects.all().count()
		group_count = Group.objects.all().count()
		
		context = {'member_count': members_count, 'group_count': group_count,}	
		return render(request, 'index.html', context)
	else:
		return redirect('/login')
    
def personal(request):
	authenticated_user = request.user
	authenticated_username = request.user.username

	if authenticated_username == 'admin':
		context = {'authenticated_username': authenticated_username,}
		return render(request, 'personal.html', context)
	else:
		authenticated_member = Member.objects.get(user=authenticated_user)
		authenticated_member_groups = Group.objects.filter(leader=authenticated_member)
		context = {'authenticated_username': authenticated_username, 'authenticated_member_groups': authenticated_member_groups,}
		return render(request, 'personal.html', context)