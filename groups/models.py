from django.db import models
from members.models import Member

class Group(models.Model):
	name = models.CharField(max_length=50)
	leader = models.ForeignKey('members.Member')
	members = models.ManyToManyField('members.Member', related_name='member_groups', blank=True)

	def __unicode__(self):
		return self.name

class Meeting(models.Model):

	# A Meeting has a type that can be either STUDY or RELATIONSHIP
	
	STUDY = 'ST'
	RELATIONSHIP = 'RE'

	MEETING_TYPE = (
			(STUDY, 'Estudo'),
			(RELATIONSHIP, 'Relacionamento'),
	)

	group = models.ForeignKey('Group')
	date = models.DateField(auto_now_add=True)
	members_who_attended = models.ManyToManyField('members.Member', blank=True)
	comments = models.TextField()
	type = models.CharField(max_length=2, choices=MEETING_TYPE, default=STUDY)

	def __unicode__(self):
		return self.group.name
